"""
Sample lib
"""
import requests

HELLO = "hello world!"


def add_one(n: int) -> int:
    """Sample function to show off tests"""
    return n + 1


def get_json() -> None:
    "sample function to use a 3rd party lib"
    resp = requests.get("https://jsonplaceholder.typicode.com/todos/1", timeout=10)
    resp.raise_for_status()
