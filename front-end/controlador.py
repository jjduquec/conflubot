import re
import requests  as r
import asyncio
pattern = r"confluence\.atlassian\.com/[a-z0-9\-]+/[a-z0-9\-]+-\d+\.html"


#getting chatbot answer  
def get_answer(query):

    #check if exist confluence link 
    if re.search(pattern,query) !=None:  
        link='https://'+(re.findall(pattern,query)[0])
        request= r.get('http://conflubot_ingestion:8081/api/get_repository/',json={'url':link})
        if request.status_code==200:
            message=(request.json())['message']
        else: 
            message="please check the ingestion component"
        #message=get_repository(link)
        
    else:  
        #message=ask_question(query)
        request=r.get('http://conflubot_retriever:8082/api/ask_question/',json={'question':query} )
        if request.status_code==200: 
            message=(request.json())['message']
        else: 
            message="please check the retriever component"

        
    return message

   
        

    
