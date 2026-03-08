
# Ollama Chatbot

A simple Python-based chatbot built using **Ollama** for running local large language models.

This project demonstrates how to interact with Ollama models using Python and implement features such as memory handling, structured output, conditional prompts, and parallel execution.

---

## Project Overview

The chatbot communicates with an Ollama model running locally and allows experimentation with different prompt strategies and response handling methods.

The project includes examples of:

* Chat prompt handling
* Conditional responses
* Structured output generation
* Memory-based conversation
* Parallel execution
* Custom model execution

---

## Features

• Chat-based interaction with Ollama models
• Conversation memory handling
• Structured response formatting
• Conditional prompt logic
• Parallel model execution
• Custom chatbot runtime logic

---

## Tech Stack

* Python
* Ollama
* Local LLM models (e.g., Llama3, Mistral)

---

## Project Structure

```
ollama-chatbot
│
├── app.py                 # Main chatbot program
├── Chatprompt.py          # Prompt handling
├── Condition.py           # Conditional logic
├── Custom_run.py          # Custom model execution
├── Structure_output.py    # Structured response format
├── memory.py              # Conversation memory
└── parallel.py            # Parallel model execution
```

---

## How It Works

1. The Python script sends a prompt to the Ollama model.
2. Ollama processes the prompt using a local LLM.
3. The model response is returned to the chatbot.
4. Additional scripts control memory, formatting, and logic flow.

---

## Requirements

* Python 3.10+
* Ollama installed
* Local model installed (example)

```
ollama run llama3
```

---

## Author

**Thara Sri**

GitHub
[https://github.com/Tharasri78](https://github.com/Tharasri78)


