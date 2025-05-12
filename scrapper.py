import re
from bs4 import BeautifulSoup
from llama_index.core import Document  

file=open('jira.html')

soup=BeautifulSoup(file,'html.parser')
title=soup.find('title')
title=title.text


main_content=soup.find('div',class_='wiki-content') 
#getting all pharaghraps  
paragraphs=main_content.find_all('p')
context=[]
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





       






