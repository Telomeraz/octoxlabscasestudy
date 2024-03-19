import requests

BASE_URL = "http://127.0.0.1:8000/"


def convert_query(query: str) -> dict:
    url = BASE_URL + "converter/"
    data = {"query": query}
    response = requests.post(
        url=url,
        json=data,
    )
    if response.status_code >= 300:
        pass
    return response.json().get("result", {})
