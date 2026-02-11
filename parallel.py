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
from langchain_core.runnables import RunnableParallel, RunnableLambda

#BASE CHAIN
#task1
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a movie summariser"),
    ("human", "Please summarize the movie in brief :{input}")
])


#task2

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)
#task3

parser = StrOutputParser()

#task4  
#RUNNNABLE LAMBDA TO CNVT STR TO DICT

def to_dict(text_prev:str)->dict:
    return{"text":text_prev}

dictionary_maker_runnable = RunnableLambda(to_dict)


# chain 1


# TASK - 1 [Prompt]

linkedin_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a LinkedIn post generator"),
    ("human", "Create a post for the following text for LinkedIn: {text}")])

# TASK - 2 [LLM]

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)
# TASK - 3 [Str Parser]

parser = StrOutputParser()

chain_linkedin = linkedin_prompt | llm| parser

# chain 1 function 
def insta_chain(text_prev:dict):
    

        # TASK - 1 [Prompt]

        Instagram_prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a LinkedIn post generator"),
            ("human", "Create a post for the following text for Instagram: {text}")])

        # TASK - 2 [LLM]

        llm = ChatGroq(
            model="llama-3.1-8b-instant",
            temperature=0
        )
        # TASK - 3 [Str Parser]

        parser = StrOutputParser()

        chain_insta =Instagram_prompt | llm| parser
        result = chain_insta.invoke(text_prev)
        return result

insta_chain_runnable = RunnableLambda(insta_chain)

#final chain to connect

final_chain=(
    prompt | 
    llm| 
    parser|
    dictionary_maker_runnable|
       RunnableParallel(branches = {"linkedin": chain_linkedin, "instagram": insta_chain_runnable})

    
    
    
)
result_final=final_chain.invoke("KGF")

print(result_final)