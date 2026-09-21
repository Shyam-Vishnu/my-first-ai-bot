from dotenv import load_dotenv
import streamlit as st

from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage


load_dotenv()

llm = ChatOpenAI(
    model="gpt-5.6-luna"
)

st.title("My First AI Bot")

if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(
            content="You are a helpful question-answering assistant."
        )
    ]


for message in st.session_state.messages[1:]:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.write(message.content)

    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.write(message.content)


question = st.chat_input("Ask me anything...")


if question:
    with st.chat_message("user"):
        st.write(question)

    st.session_state.messages.append(
        HumanMessage(content=question)
    )

    response = llm.invoke(st.session_state.messages)

    st.session_state.messages.append(response)

    with st.chat_message("assistant"):
        st.write(response.content)