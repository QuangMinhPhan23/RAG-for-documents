import streamlit as st
from sentence_transformers import SentenceTransformer
import chromadb
from pathlib import Path

# Initialize ChromaDB and model
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_collection("document")
model = SentenceTransformer('all-MiniLM-L6-v2')

def test_rag_pipeline(question):
    import openai
    query_embedding = model.encode(question).tolist()
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )
    context = "\n\n".join(results['documents'][0])
    found_docs = len(results['documents'][0])
    if found_docs == 0:
        answer = "I'm sorry, I do not know the answer to that question."
    else:
        chunk = results['documents'][0][0]
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Summarize the following text in one or two concise sentences, focusing on answering the user's question."},
                    {"role": "user", "content": f"Question: {question}\nText: {chunk}"}
                ],
            )
            answer = response['choices'][0]['message']['content'].strip()
        except Exception as e:
            answer = chunk
    return {
        'question': question,
        'sources_used': found_docs,
        'answer': answer,
        'context': context
    }

st.write("Enter your question below to query the knowledge base.")

question = st.text_input("Your question:")

if question:
    result = test_rag_pipeline(question)
    st.subheader("Answer:")
    st.write(result['answer'])
    st.subheader("Sources Used:")
    st.write(f"{result['sources_used']} documents")
    st.expander("Show retrieved context").write(result['context'])
