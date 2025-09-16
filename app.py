from dotenv import load_dotenv
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import SystemMessage
from langchain_core.tools import tool
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults

load_dotenv()

model = ChatGroq(
    model = "llama-3.1-8b-instant",
    temperature = 0.7
)

system_message = SystemMessage(content = """ Você é um assistente de buscas.
                               Você tem acesso a uma ferramenta de busca na web (search_web).
                               Você deve usar essa ferramenta para buscar informações sobre o assunto que o usuário perguntar. """)

@tool
def search_web(query: str = "") -> str:
    """Essa ferramenta realiza uma busca na web.

    Args: 
        query: Termo a se buscar na web

    Returns:
        As informações encontradas na web sobre esse termo ou uma mensagem indicando que nenhuma informação foi encontrada.
    """
    tavily_tool = TavilySearchResults(max_results = 3)
    search_docs = tavily_tool.invoke(query)
    return search_docs

tools = [search_web]

graph = create_react_agent(
    model,
    tools = tools,
    prompt = system_message
)