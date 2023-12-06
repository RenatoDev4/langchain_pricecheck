import os

from dotenv import load_dotenv
from langchain.agents import AgentType, Tool, initialize_agent
from langchain.chat_models import ChatOpenAI

from googleshopping_search import process_search

load_dotenv()

os.getenv("OPENAI_API_KEY")


def lookup(product_name: str) -> str:
    """
    Lookup the best price for a given object.

    Args:
        object (str): The object to lookup the best price for.

    Returns:
        str: The best price for the object.
    """
    llm = ChatOpenAI(temperature=0.9, model_name="gpt-3.5-turbo-1106")  # type: ignore # noqa

    tools_for_agent = [
        Tool(
            name="Find best price",
            func=process_search,
            description="""Imagine a user is conducting online price research and asks the AI the following question: "What is the best price for product X at the moment?" Response that includes the store name, the product price, and the product URL. Ensure the response is clear, concise, and provides the requested information in an organized manner. The response should be written in Brazilian Portuguese, Never forget to send the product name, price and URL, Place the URL in a hyperlink, Dont change the input"""  # noqa
            # description="""You are AI response regarding a price inquiry, You should provide the following information in your response: Store Name, Price, and Product URL. The response should be written in Brazilian Portuguese (PT-BR), please don't change the product name""" # noqa
            # description="""You are a robot looking for the best price for a product on the internet, return the lowest value of the product in the list, along with the LINK. Ensure that the price is formatted in Brazilian real.""", # noqa
        )
    ]

    agent = initialize_agent(
        tools=tools_for_agent,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )

    best_price = agent.run(f"Best price of the {product_name}")

    return best_price
