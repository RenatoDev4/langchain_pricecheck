import os

from langchain import PromptTemplate
from langchain.agents import AgentType, Tool, initialize_agent
from langchain.chat_models import ChatOpenAI

from googleshopping_search import process_search

os.environ["OPENAI_API_KEY"] = ""


def lookup(object: str) -> str:
    """
    Lookup the best price for a given object.
    
    Args:
        object (str): The object to lookup the best price for.
        
    Returns:
        str: The best price for the object.
    """
    llm = ChatOpenAI(temperature=0, model_name="gpt-4")
    
    tools_for_agent = [
        Tool(
            name="I want you to give me the product with the lowest among all",
            func=process_search,
            description="Return the lowest value of the product"
        )
    ]

    agent = initialize_agent(
        tools=tools_for_agent,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )
    
    best_price = agent.run(object)

    return best_price


if __name__ == "__main__":
    lookup("Garfo Tramontina")