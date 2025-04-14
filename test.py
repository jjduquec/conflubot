
"""
from dotenv import load_dotenv  
from huggingface_hub import InferenceClient 
import os  

#loading environment  
load_dotenv(dotenv_path=".env")
api_key=os.getenv("HF_KEY")


client = InferenceClient(

    provider="hf-inference",
    api_key=api_key,


)

file=open('context.txt','r') 
context=file.read()

answer = client.question_answering(
    question="What is the purpose of Jira?",
    context=context,
    model="distilbert/distilbert-base-cased-distilled-squad"

)


print(answer)

"""

from controlador import get_answer 


answer= get_answer("who made Jira?")
print(answer)