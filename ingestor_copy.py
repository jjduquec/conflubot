import requests 
import chromadb
from bs4 import BeautifulSoup  
from llama_index.core import Document,VectorStoreIndex,Settings,StorageContext
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

url="https://confluence.atlassian.com/jirasoftwareserver/getting-started-as-a-jira-software-user-938845161.html"

embed_model=HuggingFaceEmbedding(model_name='./all-MiniLM-L12-v2')

#setting the environment  
Settings.embed_model=embed_model
Settings.chunk_size=256
Settings.chunk_overlap=20


def save_content(context):
    #prepare DB 
    db=chromadb.PersistentClient(path="./db")
    collection=db.get_or_create_collection("confluence")
    vector_store=ChromaVectorStore(chroma_collection=collection)
    storage_context=StorageContext.from_defaults(vector_store=vector_store)

    #counting before store 
    current_registries=collection.count()

    #indexing  
    document=Document(text=context)
    VectorStoreIndex.from_documents([document],
                                    storage_context=storage_context
                                    )
    
    if(collection.count()>current_registries):
        return True
    else:  
        return False


response=requests.get(url)
if response.status_code ==200: 
    #web page content obtained  
    soup=BeautifulSoup(response.content,'html.parser')
    content=soup.find("div",class_="wiki-content")
    context=str(content.get_text())
    if(save_content(context)):
        print("saved sucessfully")
    else:  
        print("something went wrong")
 
    

    
else: 
    print("unable to query web page ")
