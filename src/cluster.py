from sentence_transformers import SentenceTransformer
from sklearn.cluster import HDBSCAN
from sklearn.preprocessing import normalize
import numpy as np
from pathlib import Path
import umap

def embed_documents(filepaths, model):
    all_doc_embeddings = []

    for path in filepaths:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
        if not text:
            continue 

        all_doc_embedding = model.encode(f"passage: {text}")
        all_doc_embeddings.append(all_doc_embedding)

    return np.vstack(all_doc_embeddings)

# LOADING MODEL
# model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')
model = SentenceTransformer('intfloat/multilingual-e5-large')

# EMBEDDING
filepaths = [str(p) for p in Path("data").glob("*") if p.is_file()]

embeddings = embed_documents(filepaths, model)
normalized_embeddings = normalize(embeddings)
reducer = umap.UMAP(n_components=15, metric="cosine")
reduced = reducer.fit_transform(normalized_embeddings)

# CLUSTERING
hdb = HDBSCAN(copy=True, min_cluster_size=2)
labels = hdb.fit_predict(normalized_embeddings)

# PRINTING RESULTS (first 50 symbols of document)
documents = []

for file in filepaths:
    with open(file, "r", encoding="utf-8") as f:
        text = f.read(100)
        documents.append(text)

documents = np.array(documents)
labels = np.array(labels)

for i in range(-1, np.max(labels)+1):
    filtered_sentences = documents[labels == i]
    print(f"\n===Sentences with label {i}===")
    for sentence in filtered_sentences:
        print(f"-{sentence}...\n")
    print(f"\n")
