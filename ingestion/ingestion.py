import requests 
import chromadb
import re
from bs4 import BeautifulSoup  
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core import Document,VectorStoreIndex,Settings,StorageContext
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.embeddings.huggingface import HuggingFaceEmbedding



embed_model=HuggingFaceEmbedding(model_name='./conflubot_model')



def save_content(documents):
    #prepare DB 
    db=chromadb.HttpClient(host='db',port=8000)
    collection=db.get_or_create_collection("dev")
    vector_store=ChromaVectorStore(chroma_collection=collection)
    storage_context=StorageContext.from_defaults(vector_store=vector_store)

    #counting before store 
    current_registries=collection.count()

    #indexing
    splitter=SentenceSplitter(chunk_size=350, chunk_overlap=35)
    VectorStoreIndex.from_documents(documents,
                                    storage_context=storage_context,
                                    embed_model=embed_model,
                                    transformations=[splitter]
                                    )
    
    if(collection.count()>current_registries):
        return True
    else:  
        raise ValueError('Context were not saved , please try again ')

#extraer contenido repositorio confluence
def get_content(url):
    context=[]
    repository=requests.get(url)
    if repository.status_code==200:
        #able to read the repository
        soup=BeautifulSoup(repository.content,'html.parser')
        title=soup.find('title')
        title=title.text
        main_content=soup.find('div',class_='wiki-content') 
        #getting all pharaghraps  
        paragraphs=main_content.find_all('p')

        for p in paragraphs:  
        #extracting content
            if p.text != '':
                content=re.sub(r'[^a-zA-Z0-9]', ' ', p.text)
                topic=p.find_previous_sibling(['h2','h3','h4'])
                #getting topic based on page titles  
                if topic !=None: 
                    topic=topic.text 
                else:  
                    topic='None'
        
                #looking for lists 
                nested_list=p.find_next_sibling(['ol','ul'])
                if nested_list !=None:  
                    nested_list=re.sub(r'[^a-zA-Z0-9]', ' ', nested_list.text)
                    content+='\n'+nested_list
                document=Document(text=content,metadata={'title':title,'topic':topic})
                context.append(document)

        return context
    else:  
        raise ValueError('Unable to read confluence repository')

def get_repository(url):
    try:
        documents=get_content(url)
        if(save_content(documents)):
            return "Repository downloaded sucessfully"
    except Exception as e :  
        return str(e)
    


