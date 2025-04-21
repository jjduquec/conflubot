from dotenv import load_dotenv
import os  
from huggingface_hub import InferenceClient

#loading environment  
load_dotenv(dotenv_path=".env")
api_key=os.getenv("HF_KEY")



#getting chatbot answer  
def get_answer(question):
    
    #getting Inference Client 
    client=InferenceClient(
    provider="hf-inference",
    api_key=api_key,


    )

    file=open("context.txt",'r')
    context=file.read()
    file.close()
    answer=client.question_answering(
        question=question,
        context=context,
        model="distilbert/distilbert-base-cased-distilled-squad"


    )

    return answer['answer']

    



