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
from langchain_core.runnables import RunnableLambda


#task1
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful teacher"),
    ("human", "{input}")
])


#task2

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)
#task3

parser = StrOutputParser()

#task4

def to_dict(text_prev:str)->dict:
    return{"text_key":text_prev}

dictionary_maker_runnable = RunnableLambda(to_dict)
# TASK - 5 [Template For Post]

prompt_post = ChatPromptTemplate.from_messages(
    messages=[
        ("system", "You're a social media post generator. "),
        ("human", "Create a post for the following text for LinkedIn: {text_key}"),
    ]
)

#task6

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)
#task7

parser = StrOutputParser()

chain = prompt | llm | parser |  dictionary_maker_runnable | prompt_post | llm| parser


result = chain.invoke({"input": "Artificial Intelligence"})


print(result)