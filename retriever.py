import chromadb 
from llama_index.core import VectorStoreIndex
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore

#model for embedding
embed_model=HuggingFaceEmbedding(model_name='./all-MiniLM-L12-v2')


def get_context(query): 
    client = chromadb.PersistentClient("./db")
    collection=client.get_or_create_collection("dev")
    vectore_store=ChromaVectorStore(chroma_collection=collection) 
    index=VectorStoreIndex.from_vector_store(
    vector_store=vectore_store,
    embed_model=embed_model
    )

    retriever=index.as_retriever(similarity_top_k=3)
    nodes=retriever.retrieve(query)
    context=""
    for node in nodes:  
        context+="\n"+node.text 
    return context


