from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7
)

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a strict technical tutor."),
    ("human", "Explain {topic} clearly.")
])

messages = chat_prompt.format_messages(topic="LangChain")

response = llm.invoke(messages)

print(response.content)
