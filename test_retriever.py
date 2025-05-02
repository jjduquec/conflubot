import chromadb 
from llama_index.core import VectorStoreIndex,Settings
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore

embed_model=HuggingFaceEmbedding(model_name='./all-MiniLM-L12-v2')

#setting the environment  


#getting data from chromadb  
client = chromadb.PersistentClient("./db")
collection=client.get_or_create_collection("confluence")
vectore_store=ChromaVectorStore(chroma_collection=collection) 
index=VectorStoreIndex.from_vector_store(
    vector_store=vectore_store,
    embed_model=embed_model
)


#consultar : https://medium.com/@mayadakhatib/rag-a-simple-practical-example-using-llama-index-and-huggingface-fab3e5aa7442