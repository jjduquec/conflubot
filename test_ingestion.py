import chromadb 
from llama_index.core import Document,Settings,StorageContext,VectorStoreIndex
from llama_index.core.node_parser import SentenceSplitter  
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.embeddings.huggingface import HuggingFaceEmbedding 
from llama_index.llms.huggingface_api import HuggingFaceInferenceAPI

HF_TOKEN="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"
embed_model=HuggingFaceEmbedding(model_name="./all-MiniLM-L12-v2")
llm = HuggingFaceInferenceAPI(model_name="Qwen/Qwen3-235B-A22B", token=HF_TOKEN)


context="""
Jira is a powerful project management tool developed by Atlassian, 
primarily used for software development, issue tracking,
and agile project management. It enables teams to plan, track, 
and manage tasks efficiently, offering features like customizable workflows, 
real-time collaboration, and integrations with various development tools. 
Originally designed for bug tracking, Jira has evolved into a comprehensive solution for organizing projects across multiple industries, 
supporting methodologies like Scrum and Kanban. Its flexibility allows teams to tailor the platform to their specific needs, 
enhancing productivity and transparency in project execution.
"""
"""
prueba de query engine 

#prepare db
db_client=chromadb.EphemeralClient() 
collection=db_client.get_or_create_collection("test")
vectorStore=ChromaVectorStore(chroma_collection=collection)
storage_context=StorageContext.from_defaults(vector_store=vectorStore)

#preparing to store
documents=[Document(text=context)]

#storing
index=VectorStoreIndex.from_documents(
    documents,
    storage_context=storage_context,
    embed_model=embed_model
    
)

#querying about
query_engine=index.as_query_engine(llm=llm)
response=query_engine.query("Who made jira?")
print(response)
print(type(response))

"""

db_client=chromadb.PersistentClient(path="./db") 
collection=db_client.get_or_create_collection("confluence")
vectorStore=ChromaVectorStore(chroma_collection=collection)
index=VectorStoreIndex.from_vector_store(
    vector_store=vectorStore,
    embed_model=embed_model
) 

query_engine=index.as_query_engine(llm=llm)
response=query_engine.query("How to create a branch in Jira?")
print(response)
