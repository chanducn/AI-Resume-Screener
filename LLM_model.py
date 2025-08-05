from job_desc_emb import retrieve_top_chunks



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
formatted_prompt = prompt_template.format(
    job_description=job_text,
    resume_chunks="\n".join(matched_chunks[resume_name])
)
