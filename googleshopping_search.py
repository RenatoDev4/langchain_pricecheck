import json
import os
import re
from typing import Dict, List
from unicodedata import normalize

from dotenv import load_dotenv
from serpapi import GoogleSearch

load_dotenv()

api_key_serpapi = os.getenv("SERPAPI_KEY")


def search_object(product_name: str) -> str:
    """
    Get shopping results from Google Shopping API.

    Args:
        object (str): The object to search for.

    Returns:
        str: A JSON string containing the shopping results.
    """
    params = {
        "engine": "google_shopping",
        "q": product_name,
        "location_requested": "Brazil",
        "location_used": "Brazil",
        "hl": "pt",
        "gl": "br",
        "device": "desktop",
        # "num": "27",
        "google_domain": "google.com.br",
        "api_key": api_key_serpapi,
        "tbs": "mr:1,merchagg:g227476643%7Cm106916823|m7139546|g100469737%7Cm100713375|g134886126%7Cm134880504%7Cm134942054|g264499098%7Cm276949139%7Cm8231017|m482593868|m11172672|m143590035|m114573998|g227476643%7Cm106916823|",  # noqa
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    if "shopping_results" not in results:
        raise ValueError("No results found in search")

    shopping_results = results["shopping_results"]

    extracted_results = []

    for item in shopping_results:
        result_entry = {
            "title": item.get("title", ""),
            "link": item.get("link", ""),
            "extracted_price": item.get("extracted_price", ""),
        }
        extracted_results.append(result_entry)

    json_result = json.dumps(extracted_results, ensure_ascii=False)

    return json_result


def clean_text(text: str) -> str:
    """
    Cleans the given text by removing any characters that are not alphanumeric,
    whitespace, comma, period, semicolon, or common symbols in PT-BR.

    Parameters:
        text (str): The text to be cleaned.

    Returns:
        str: The cleaned text.
    """
    url_regex = r"https?://\S+|www\.\S+"

    cleaned_text = re.sub(
        rf"[^a-zA-Z0-9\s.,;áàâãéèêíìîóòôõúùûç]|({url_regex})",
        lambda match: match.group(1) if match.group(1) else "",
        normalize("NFD", text),
    )

    return cleaned_text


def extract_data(
    product_list: List[Dict[str, str]], target_product: str
) -> List[Dict[str, str]]:  # noqa
    """
    Extracts data from a given list of products without cleaning the text.

    Parameters:
        - product_list (list): A list of dictionaries representing the products. Each dictionary should have the following keys: # noqa
            - "title" (str): The title of the product.
            - "link" (str): The link to the product.
            - "extracted_price" (str): The extracted price of the product.

    Returns:
        list: A list of dictionaries representing the uncleaned results. Each dictionary will have the following keys:
            - "Title" (str): The uncleaned title of the product.
            - "Link" (str): The uncleaned link to the product.
            - "Preço" (str): The uncleaned price of the product.
    """

    filtered_results = []

    for item in product_list:
        if target_product.lower() in item.get("title", "").lower():
            filtered_results.append(
                {
                    "Title": item.get("title", ""),
                    "Url": item.get("link", ""),
                    "Price": float(str(item.get("extracted_price", "0"))),
                }
            )

    if not filtered_results:
        return []

    min_price_item = min(filtered_results, key=lambda x: x["Price"])

    return [min_price_item]


def process_search(product_name: str) -> None:
    """
    Retrieves search results for a given product name, processes the results, and prints the relevant information. # noqa

    Parameters:
    - product_name (str): The name of the product to search for.

    Returns:
    - None

    This function retrieves search results for the specified product name using the search_object function.
    The search results are then parsed and cleaned using the json.loads and extract_data functions, respectively.
    Finally, the cleaned search results are iterated over, and the title, link, and price information for each entry is printed.
    """
    json_result = search_object(product_name)
    result_list = json.loads(json_result)
    cleaned_result = extract_data(result_list, product_name)

    return cleaned_result  # type: ignore
