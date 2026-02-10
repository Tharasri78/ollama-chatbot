from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from pydantic import BaseModel, Field
from typing import TypedDict 

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

# -------- RAW OUTPUT (for inspection) --------
raw = llm.invoke(
    "Tell me a joke. Generate the output in key-value pair format with keys: setup, punchline"
)
print(raw.content)

# -------- STRUCTURED OUTPUT (for logic) --------
class JokeSchema(BaseModel):
    setup: str = Field(description="The setup for the joke")
    punchline: str = Field(description="The punchline for the joke")

structured_llm = llm.with_structured_output(JokeSchema)
                                   #(self,input) input="Tell me a joke" it takes parameter automatically
structured = structured_llm.invoke("Tell me a joke")

structured.punchline



## TYPEDICT
class llm_schema_td(TypedDict):
    setup: str
    punchline: str

llm_structured_typed_dict = llm.with_structured_output(llm_schema_td)

result = llm_structured_typed_dict.invoke("Tell me a joke")
result
