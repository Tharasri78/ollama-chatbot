# Ollama LangChain Chatbot (Gemma 4B)

A simple chatbot built using **LangChain**, **Ollama**, and **Streamlit**, running fully **locally** with the **Gemma 4B** model.  
No OpenAI API key. No paid services.

---

## Features
- Runs locally using Ollama
- Uses Gemma 4B LLM
- Streamlit-based UI
- LangChain prompt chaining
- Free and offline-friendly

---

## Tech Stack
- Python
- LangChain
- Ollama
- Streamlit
- Gemma 4B

---

## Prerequisites
Make sure you have the following installed:

- Python 3.10+
- Ollama → https://ollama.com
- Git

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/Tharasri78/ollama-chatbot.git
cd ollama-chatbot

2. Create and activate virtual environment
python -m venv env

Windows
env\Scripts\activate

macOS / Linux
source env/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Pull the Gemma model
ollama pull gemma3:4b

5. Run the application
python -m streamlit run app.py

The application will be available at:
http://localhost:8501

Author
Tharasri


---

### Next step
Save the file as `README.md`, then run:
```bash
git add README.md
git commit -m "Add README"
git push origin main
