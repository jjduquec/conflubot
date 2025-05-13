import re
from ingestion import get_repository
from retriever import ask_question

pattern = r"confluence\.atlassian\.com/[a-z0-9\-]+/[a-z0-9\-]+-\d+\.html"


#getting chatbot answer  
def get_answer(query):

    #check if exist confluence link 
    if re.search(pattern,query) !=None:  
        link='https://'+(re.findall(pattern,query)[0])
        message=get_repository(link)
        return message
    else:  
        message=ask_question(query)
        return message

   
        

    
