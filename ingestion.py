import requests 
import chromadb
import re 
from bs4 import BeautifulSoup  
from llama_index.core import Document,VectorStoreIndex,Settings,StorageContext
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.embeddings.huggingface import HuggingFaceEmbedding



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
        raise ValueError('Context were not saved , please try again ')

#extraer contenido repositorio confluence
def get_content(url): 
    #validación del enlace
    if re.search('confluence.atlassian',url) ==None : 
        raise ValueError('Url doesnt match with a confluence repository')
    else:
        #agregando el https
        pos=url.find("confluence")
        url="https://"+url[pos:]
        confluence_request=requests.get(url)
        if confluence_request.status_code==200:
            soup=BeautifulSoup(confluence_request.content,'html.parser')
            content=soup.find("div",class_="wiki-content")
            content=str(content.get_text())
            return content

        else:  
            raise ValueError('Unable to access to confluence repository')

def get_repository(url):
    try:
        context=get_content(url)
        if(save_content(context)):
            return "Repository downloaded sucessfully"
    except Exception as e :  
        return e 