import streamlit as st  

#creating chat history  
if "messages" not in st.session_state:
    st.session_state.messages=[]
    
    #initialize chatbot  
    st.session_state.messages.append({"role":"assistant","content":"Hi, How can i help?"})

def save_message(role,content):
    st.session_state.messages.append({"role":role,"content":content})

def display_message(role,message): 
    with st.chat_message(role):
        st.markdown(message)

#----------- Display zone ----------------------------------------------------




#display chat history  
for message in st.session_state.messages: 
    display_message(message["role"],message["content"])

#display user input messages  

user_message = st.chat_input("Ask something")

if user_message:  
    #display message after user input  
    display_message('user',user_message)
    save_message("user",user_message) 

    #displaying chatbot message 
    #chatbot_message= f"Conflubot: {user_message}"

    display_message('assistant',user_message)

    save_message("assistant",user_message)

    

