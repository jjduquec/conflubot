import chromadb 
from transformers import pipeline
from llama_index.core import VectorStoreIndex
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore

#model for embedding
embed_model=HuggingFaceEmbedding(model_name='./models/all-MiniLM-L6-v2')
qa_model="./distilbert-base-cased-distilled-squad"

def get_answer(query,context):  
    qa_engine=pipeline('question-answering',model=qa_model,tokenizer=qa_model)
    answer=qa_engine(context=context,question=query)
    answer=answer['answer']
    return answer

def get_context(query): 
    client = chromadb.PersistentClient("./db")
    collection=client.get_collection("dev")
    print(collection)
    vectore_store=ChromaVectorStore(chroma_collection=collection) 
    index=VectorStoreIndex.from_vector_store(
    vector_store=vectore_store,
    embed_model=embed_model
    )
    retriever=index.as_retriever()
    print(retriever)
    nodes=retriever.retrieve(query)
    context=""
    for node in nodes:  
        context+="\n"+node.text 
    return context


def  ask_question(question):
    context=get_context(question)
    answer=get_answer(question,context)
    return answer