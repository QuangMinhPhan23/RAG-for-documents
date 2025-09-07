import os
import chromadb
from sentence_transformers import SentenceTransformer
from pathlib import Path

# Initialize systems
# Connecting to chromadb
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_collection("document")

# Loading Semantic Processor
model = SentenceTransformer('all-MiniLM-L6-v2')

# Process documents
doc_count = 0
total_chunks = 0

for category in Path('document').iterdir():
    for doc in category.glob('*.txt'):
        print(f"  {doc.name}", end="")

        with open(doc, 'r', encoding="utf-8") as f:
            content = f.read()

        # Apply chunking
        chunks = [content[i:i+500] for i in range(0, len(content), 400)]

        for i, chunk in enumerate(chunks):
            doc_id = f"{doc.stem}_{i}"
            # Apply embedding
            embedding = model.encode(chunk).tolist()

            # Store in database
            collection.add(
                ids=[doc_id],
                embeddings=[embedding],
                documents=[chunk],
                metadatas={"file": doc.name}
            )
            total_chunks += 1

        doc_count += 1
        print(f" ({len(chunks)} chunks)")


print(f"Statistics:")
print(f"   • Documents processed: {doc_count}")
print(f"   • Knowledge chunks: {total_chunks}")

def test_rag_pipeline(question):
    print(f" Question: '{question}'")
    query_embedding = model.encode(question).tolist()
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )
    print(f"   Found {len(results['documents'][0])} relevant documents!")
    context = "\n\n".join(results['documents'][0])
    # Improved response logic
    found_docs = len(results['documents'][0])
    if found_docs == 0:
        answer = "I'm sorry, I do not know the answer to that question."
    else:
        # Use the most relevant chunk as the answer
        answer = results['documents'][0][0]
    return {
        'question': question,
        'sources_used': found_docs,
        'answer': answer
    }

test_question = "What is paraphrase?"
result = test_rag_pipeline(test_question)

print(f" Question: {result['question']}")
print(f" Sources Used: {result['sources_used']} documents")
print(f" Answer: {result['answer']}")