
# Agente Simples com LangGraph

Este projeto demonstra um agente simples utilizando a biblioteca LangGraph para fluxos de trabalho de IA.

## O que o agente faz?

O agente atua como um assistente de buscas. Ele recebe perguntas do usuário e utiliza uma ferramenta de busca na web para encontrar informações relevantes sobre o assunto solicitado. O agente utiliza o modelo Llama-3.1-8b-instant via Groq e faz buscas na web usando a API Tavily, retornando as informações encontradas ao usuário.

## Descrição

O objetivo deste projeto é apresentar um exemplo básico de como criar e executar um agente utilizando LangGraph, facilitando a compreensão de fluxos de decisão e execução em aplicações de IA.

## Estrutura do Projeto

- `app.py`: Script principal do agente.
- `requirements.txt`: Dependências necessárias para executar o projeto.
- `langgraph.json`: Configuração do fluxo LangGraph.
- `.env_example`: Exemplo de variáveis de ambiente necessárias.

## Como Executar

1. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Crie o arquivo `.env`:**
   - Copie o arquivo `.env_example` e renomeie para `.env`.
   - Preencha as chaves de API necessárias (`GROQ_API_KEY` e `TAVILY_API_KEY`) com seus valores.
3. **Execute o agente usando LangSmith:**
   ```bash
   langgraph dev
   ```

## Requisitos
- Python 3.11 ou superior
- Bibliotecas listadas em `requirements.txt`
