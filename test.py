import chromadb 
from ingestion import get_repository
from retriever import get_context

def clean_db(): 
    client=chromadb.PersistentClient(path='./db')
    client.delete_collection('dev') 

#clean_db()
url='https://confluence.atlassian.com/jirasoftwareserver/getting-started-as-a-jira-software-user-938845161.html'
query='what is the easiest way to view information about a project?'
message=get_repository(url)
print(message)


