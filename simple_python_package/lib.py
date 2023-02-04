"""
Sample lib
"""
import requests

HELLO = "hello world!"


def get_json() -> None:
    "get some sample JSON"
    resp = requests.get("https://jsonplaceholder.typicode.com/todos/1", timeout=10)
    resp.raise_for_status()
