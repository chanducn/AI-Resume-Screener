from sentence_transformers import SentenceTransformer
import numpy as np  

# first we hvae to make chunks of senteces
def chunk_text(text,chunk_size=300):
    """
    Splits the input text into chunks of specified size.
    
    Args:
        text (str): The input text to be chunked.
        chunk_size (int): The maximum size of each chunk. Default is 300 characters.
        
    Returns:
        list: A list of text chunks.
    """
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])
    return chunks

# Create Embedding
embm = SentenceTransformer('all-MiniLM-L6-v2')

def embed_chunks(chunks):
    return embm.encode(chunks)


def process_all_resumes(resume_texts_dict):
    all_emdb = {}
    all_chunks = {}

    for filename,text in resume_texts_dict.items():
        chunks = chunk_text(text)
        embedding = embed_chunks(chunks)
        all_chunks[filename] = chunks
        all_emdb[filename] = np.array(embedding)
        print(f"✅ Processed {filename}: {len(chunks)} chunks")

    import pickle

    with open("resume_chunks.pkl", "wb") as f:
        pickle.dump(all_chunks, f)

    with open("resume_embeddings.pkl", "wb") as f:
        pickle.dump(all_emdb ,f)


    return all_chunks, all_emdb
