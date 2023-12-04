import json
import re

from serpapi import GoogleSearch


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
        "num": "30",
        "google_domain": "google.com.br",
        "api_key": "3aec8378ee805935c1e0d4d99f0118828199bd33f85289ed93aae40c31f8de5c",
    }

    search = GoogleSearch(params)
    results = search.get_dict()
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


def clean_text(text):
    """
    Cleans the given text by removing any characters that are not alphanumeric, whitespace, comma, period, or semicolon.

    Parameters:
        text (str): The text to be cleaned.

    Returns:
        str: The cleaned text.
    """
    cleaned_text = re.sub(r'[^a-zA-Z0-9\s.,;]', '', text)
    return cleaned_text


def extract_data(product_list):
    """
    Extracts data from a given list of products.

    Parameters:
        - product_list (list): A list of dictionaries representing the products. Each dictionary should have the following keys:
            - "title" (str): The title of the product.
            - "link" (str): The link to the product.
            - "extracted_price" (str): The extracted price of the product.

    Returns:
        list: A list of dictionaries representing the cleaned results. Each dictionary will have the following keys:
            - "Titulo" (str): The cleaned title of the product.
            - "Link" (str): The cleaned link to the product.
            - "Preço" (str): The cleaned price of the product.
    """
    cleaned_results = []

    for item in product_list:
        cleaned_entry = {
            "Titulo": clean_text(item.get("title", "")),
            "Link": clean_text(item.get("link", "")),
            "Preço": clean_text(str(item.get("extracted_price", ""))),
        }
        cleaned_results.append(cleaned_entry)

    return cleaned_results

def process_search(product_name):
    """
    Retrieves search results for a given product name, processes the results, and prints the relevant information.

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
    cleaned_result = extract_data(result_list)

    for entry in cleaned_result:
        print(f"Titulo: {entry['Titulo']}")
        print(f"Link: {entry['Link']}")
        print(f"Preço: R$ {entry['Preço']}")