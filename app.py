import gradio as gr
from job_desc import get_job_desc, load_job_desc
from extractor import extract_pdf
from Chunking_and_Embedding import process_all_resumes
from sentence_transformers import SentenceTransformer
from job_desc_emb import embed_job_desc, retrieve_top_chunks
from groq import Groq
import os

def pipeline(job_desc_text, job_desc_file, resume_files):
    # 1. Get job description (prefer file if provided)
    if job_desc_file is not None:
        job_text = job_desc_file.decode("utf-8")
    elif job_desc_text.strip():
        job_text = job_desc_text
    else:
        return "❌ Please provide a job description (paste or upload).", ""
    
    # 2. Parse resumes from uploaded files
    if not resume_files or len(resume_files) == 0:
        return "❌ Please upload at least one PDF resume.", ""
    resume_texts = {}
    for file in resume_files:
        text = extract_pdf(file.name)
        resume_texts[os.path.basename(file.name)] = text
    if not resume_texts:
        return "❌ No resumes could be parsed.", ""
    
    # 3. Chunk and embed resumes
    all_chunks, all_embeddings = process_all_resumes(resume_texts)
    
    # 4. Embed job description
    embm = SentenceTransformer('all-MiniLM-L6-v2')
    job_embedding = embed_job_desc(job_text, embm)
    
    # 5. Retrieve top-matching chunks for each resume
    matched_chunks = retrieve_top_chunks(job_embedding, all_chunks, all_embeddings, top_k=5)
    
    # 6. LLM scoring
    prompt_template = """
You are an HR expert shortlisting candidates for the following job role:

JOB DESCRIPTION:
{job_description}

CANDIDATE RESUME SNIPPETS:
{resume_chunks}

TASK:
Score the candidate from 1 to 10 for how well they match the job. Give a short reason for your rating.

Output format:
Score: <number>
Reason: <one-liner explanation>
"""
    groq_api_key = os.getenv("GROQ_API_KEY", "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") 
    groq = Groq(api_key=groq_api_key)

    results = []
    for resume_name in matched_chunks:
        formatted_prompt = prompt_template.format(
            job_description=job_text,
            resume_chunks="\n".join(matched_chunks[resume_name])
        )
        response = groq.chat.completions.create(
            model="gemma2-9b-it",
            messages=[
                {"role": "system", "content": "You are an HR expert shortlisting candidates."},
                {"role": "user", "content": formatted_prompt}
            ]
        )
        llm_output = response.choices[0].message.content
        results.append(f"**{resume_name}**\n{llm_output}\n")

    return "✅ Scoring complete!", "\n---\n".join(results)

with gr.Blocks() as demo:
    gr.Markdown("# 📝 AI Resume Screener")
    with gr.Row():
        job_desc_text = gr.Textbox(label="Paste Job Description", lines=8, placeholder="Paste job description here...")
        job_desc_file = gr.File(label="Or Upload Job Description (.txt)", file_types=[".txt"])
    resume_files = gr.Files(label="Upload Resume PDFs", file_types=[".pdf"])
    run_btn = gr.Button("Run Screening")
    status = gr.Markdown()
    results = gr.Markdown()

    run_btn.click(
        pipeline,
        inputs=[job_desc_text, job_desc_file, resume_files],
        outputs=[status, results]
    )

if __name__ == "__main__":
    demo.launch()