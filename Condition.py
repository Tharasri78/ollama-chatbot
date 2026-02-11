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
from langchain_core.runnables import RunnableParallel, RunnableLambda,RunnableBranch

#BASE CHAIN
from pydantic import BaseModel
from typing import Literal
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)
class llm_schema(BaseModel):
    movie_summary_flag: Literal["positive", "negative"]

llm_structured_output = llm.with_structured_output(llm_schema)

#task1
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a movie summariser"),
    ("human", "Please categorize the movie review as positive or negative : {input}")
])


#task2

llm_structured_output = llm.with_structured_output(llm_schema)



#task4  
#RUNNNABLE LAMBDA TO CNVT STR TO DICT


def pydantic_json(input:llm_schema)-> str:

    return input.model_dump()['movie_summary_flag']

pydantic_json_lambda = RunnableLambda(pydantic_json)


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
conditional_chain = RunnableBranch(
    (lambda x: "positive" in x, chain_linkedin),
     insta_chain_runnable
)
final_chain=(
    prompt | 
    llm_structured_output | 
    pydantic_json_lambda|
    conditional_chain

    
    
    
)
result_final=final_chain.invoke({"input": "I loved this KGF movie"})

print(result_final)