from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st

from dotenv import load_dotenv

load_dotenv()

#Prompt Template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant.please response to the user queries"),
        ("user","Question:{question}")
    ]
)

#Streamlit Framework

st.title("LangChain with Ollama..")
input_txt=st.text_input("Search the topic u want")

#Ollama 
llm=Ollama(model="gemma3:4b")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_txt:
    st.write(chain.invoke({"question":input_txt}))