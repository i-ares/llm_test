import streamlit as st

from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain.chat_models import ChatOpenAI

#streamlit UI
st.set_page_config(page_title = "Your Personal Professor")
st.header("What problem may I solve for you today?")

from dotenv import load_dotenv
load_dotenv()
import os

chat=ChatOpenAI(openai_api_key=os.environ["OPEN_API_KEY"],temperature=0.45) #add you personal open api key in this section

if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages']=[
        SystemMessage(content="You are a professor like AI assistant")
    ]

## Function to load OpenAI and chat
def get_chat_response(question):
    st.session_state['flowmessages'].append(HumanMessage(content=question))
    answer = chat(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(AIMessage(content=answer.content))
    return answer.content

input = st.text_input("Input: ", key="input")
response = get_chat_response(input)

submit=st.button("What's up with you today?")

if submit:
    st.subheader("The response is")
    st.write(response)
