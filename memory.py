# ===============================
# LOAD ENV VARIABLES
# ===============================
from dotenv import load_dotenv
load_dotenv()

# ===============================
# IMPORTS
# ===============================
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_classic.memory import ConversationSummaryBufferMemory
from langchain_classic.chains import LLMChain

# ===============================
# MODEL
# ===============================
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.5
)

# ===============================
# MEMORY
# ===============================
memory = ConversationSummaryBufferMemory(
    llm=llm,
    memory_key="history",
    max_token_limit=150
)

# ===============================
# PROMPT
# ===============================
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "{history}\nUser: {input}")
])

# ===============================
# OUTPUT PARSER
# ===============================
parser = StrOutputParser()

# ===============================
# CHAIN
# ===============================
chain = LLMChain(
    llm=llm,
    prompt=prompt,
    memory=memory,
    output_parser=parser
)

# ===============================
# CHAT LOOP
# ===============================
print("Chatbot started. Type 'exit' to stop.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    response = chain.invoke({"input": user_input})
    print("AI:", response)
