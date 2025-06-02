import chromadb 
from ollama import Client
from llama_index.core import VectorStoreIndex
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore

#model for embedding
embed_model=HuggingFaceEmbedding(model_name='./conflubot_model')


def get_answer(query,context): 
    client=Client(host='http://llm:11434')
    prompt=f"""
    you are an ai assistant to search information in confluence repositories\
    based on the next context : {context} \
    answer the next question : {query}\
    if you dont know the answer , just return as an answer : sorry, i dont have information about it\
    """
    response=client.chat(model='qwen2:1.5b',messages=[{
    'role':'user',
    'content': prompt,
    }])
 
    return response['message']['content']

def get_context(query): 
    client =chromadb.HttpClient(host='db',port=8000)
    collection=client.get_collection("prod")
    vectore_store=ChromaVectorStore(chroma_collection=collection) 
    index=VectorStoreIndex.from_vector_store(
    vector_store=vectore_store,
    embed_model=embed_model
    )
    retriever=index.as_retriever(
        similarity_top_k=1
    )
    nodes=retriever.retrieve(query)
    context=""
    if len(nodes)>0:
        context=nodes[0].get_text()
    
    
    return context


def  ask_question(question):
    context=get_context(question)
    answer=get_answer(question,context)
    return answer



