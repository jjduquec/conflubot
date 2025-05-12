import requests  
from bs4 import BeautifulSoup

url="https://confluence.atlassian.com/jirasoftwareserver/using-jira-applications-with-advanced-roadmaps-for-jira-939938820.html"
repository=requests.get(url) 
soup=BeautifulSoup(repository.content,'html.parser')
main_content=soup.find('div',class_='wiki-content')

#trying to find first H2  
if main_content.find('h2') != None:  
    sections=main_content.find_all('h2')
    test=sections[0] 
    section_content=test.find_all('p')
    print(section_content)