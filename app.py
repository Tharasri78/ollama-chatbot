# ===============================
# LOAD ENV VARIABLES
# ===============================

from dotenv import load_dotenv
load_dotenv()


# ===============================
# IMPORTS
# ===============================

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq


# ===============================
# PROMPT TEMPLATE
# ===============================

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful teacher"),
    ("human", "Explain what is {topic} in very simple words")
])


# ===============================
# MODEL
# ===============================

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)


# ===============================
# OUTPUT PARSER
# ===============================

parser = StrOutputParser()


# ===============================
# LCEL PIPELINE
# ===============================

chain = prompt | llm | parser


# ===============================
# RUN THE CHAIN
# ===============================

result = chain.invoke({"topic": "Artificial Intelligence"})

print(result)

# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser
# from langchain_groq import ChatGroq
# import streamlit as st
# import os
# from dotenv import load_dotenv

# load_dotenv()

# #Prompt Template

# prompt=ChatPromptTemplate.from_messages(
#     [
#         ("system","You are a helpful assistant.please response to the user queries"),
#         ("user","Question:{question}")
#     ]
# )

# #Streamlit Framework

# st.title("LangChain with groq..")
# input_txt=st.text_input("Search the topic u want")

# #groq
# llm = ChatGroq(
#     model="llama-3.1-8b-instant",
#     temperature=0
# )

# output_parser=StrOutputParser()
# chain=prompt|llm|output_parser

# if input_txt:
    
#     st.write(chain.invoke({"question":input_txt}))