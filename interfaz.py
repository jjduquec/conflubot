import streamlit as st 

st.title("Conflubot")

#chat history
if "messages" not in st.session_state:
    st.session_state.messages=[]

#display messages  
for message in st.session_state.messages: 
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#initialize chat 
with st.chat_message("assistant"):
    st.markdown("Hi, how can i help?")
    st.session_state.messages.append({"role":"assistant","content":"Hi, how can i help?"})

if prompt :=st.chat_input("Ask something"):
    st.chat_message("user").markdown(prompt)
    #saving user message
    st.session_state.messages.append({"role":"user","content":prompt})

    """
        Add here functions to gen bot response
    """

    response = f"Conflubot:{prompt}"

    with st.chat_message("assistant"): 
        st.markdown(response)
    
    #saving assistant messages
    st.session_state.messages.append({"role":"assistant","content":response})