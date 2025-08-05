import faiss
import numpy as np






def embed_job_desc(text,model):
    return model.encode([text])[0] #returns a 384 dimensional vector

def retrieve_top_chunks(job_embedding,all_chunks,all_embeddings,top_k=5):
    matched_chunks = {}

    for filename in all_chunks:
        chunk_list = all_chunks[filename]
        embed_array = all_embeddings[filename]

        index = faiss.IndexFlatL2(embed_array.shape[1])
        index.add(embed_array)

        D,I = index.search(np.array([job_embedding]),top_k) # Distance and indices
        retrieved = [chunk_list[i] for i in I[0]]
        matched_chunks[filename] = retrieved
        print(f"🔍 Retrieved top {top_k} chunks for {filename}")

    return matched_chunks
