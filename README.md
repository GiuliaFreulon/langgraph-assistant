
# Simple Agent with LangGraph

This project demonstrates a simple agent using the LangGraph library for AI workflow orchestration.

## What does the agent do?

The agent acts as a search assistant. It receives user questions and uses a web search tool to find relevant information about the requested topic using the Tavily API, returning the information found to the user.

## Description

The goal of this project is to present a basic example of how to create and run an agent using LangGraph, making it easier to understand decision and execution flows in AI applications.

## Project Structure

- `app.py`: Main agent script.
- `requirements.txt`: Project dependencies.
- `langgraph.json`: LangGraph flow configuration.
- `.env_example`: Example of required environment variables.

## How to Run

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Create the `.env` file:**
   - Copy the `.env_example` file and rename it to `.env`.
   - Fill in the required API keys (`GROQ_API_KEY` and `TAVILY_API_KEY`) with your values.
3. **Run the agent using LangSmith:**
   ```bash
   langgraph dev
   ```

## Requirements
- Python 3.11 or higher
- Libraries listed in `requirements.txt`
