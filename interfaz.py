import streamlit as st 
import random

st.title("Conflubot")

bot_responses=[
    "Im an old man",
    "Where do you live?",
    "What do you want?",
    "Can you just stop?"
]

def get_resposne():
    i=random.randint(0,len(bot_responses)-1)
    return bot_responses[i]

#create chat history
if "messages" not in st.session_state:
    st.session_state.messages=[]

#display messages  
for message in st.session_state.messages: 
    with st.chat_message(message["role"]):
        st.markdown(message["content"])






#initialize chat 
with st.chat_message("assistant"): 
    st.session_state.messages.append({"role":"assistant","content":"Hi, how can i help?"})
    st.markdown("Hi, how can i help?")

if prompt :=st.chat_input("Ask something"):
    st.chat_message("user").markdown(prompt)
    #saving user message
    st.session_state.messages.append({"role":"user","content":prompt})

    
    # Add here functions to gen bot response
    
    bot_response=get_resposne()
    response = f"Conflubot:{bot_response}"

#    with st.chat_message("assistant"): 
#        st.markdown(response)
    
    #saving assistant messages
    st.session_state.messages.append({"role":"assistant","content":response})


