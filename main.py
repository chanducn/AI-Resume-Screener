from job_desc import get_job_description
from extractor import select_folder_gui, parse_resumes
from Chunking_and_Embedding import process_all_resumes
from sentence_transformers import SentenceTransformer
from job_desc_emb import embed_job_desc, retrieve_top_chunks
from groq import Groq
import os

# 1. Get job description
job_text = get_job_description()
if not job_text.strip():
    print("❌ No job description provided. Exiting.")
    exit(1)

# 2. Select and parse resumes
resume_folder = select_folder_gui()
if not resume_folder:
    print("❌ No resume folder selected. Exiting.")
    exit(1)
resume_texts = parse_resumes(resume_folder)
if not resume_texts:
    print("❌ No resumes found. Exiting.")
    exit(1)

# 3. Chunk and embed resumes
all_chunks, all_embeddings = process_all_resumes(resume_texts)

# 4. Embed job description
embm = SentenceTransformer('all-MiniLM-L6-v2')
job_embedding = embed_job_desc(job_text, embm)

# 5. Retrieve top-matching chunks for each resume
matched_chunks = retrieve_top_chunks(job_embedding, all_chunks, all_embeddings, top_k=5)

# 6. Format prompt for each candidate (LLM scoring)
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

groq_api_key = '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'
groq = Groq(api_key=groq_api_key)

for resume_name in matched_chunks:
    formatted_prompt = prompt_template.format(
        job_description=job_text,
        resume_chunks="\n".join(matched_chunks[resume_name])
    )
    print(f"\n--- Prompt for {resume_name} ---\n")
    print(formatted_prompt)
    # Send `formatted_prompt` to your LLM and process the response
    response = groq.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an HR expert shortlisting candidates."},
            {"role": "user", "content": formatted_prompt}
        ]
    )
    print("\nLLM Response:\n")
    print(response.choices[0].message.content)

print("\n✅ Pipeline complete. Ready for LLM scoring.")
