from typing import Iterator

import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.fixture(scope="session")
def base_url() -> str:
    return BASE_URL


@pytest.fixture(scope="session")
def posts_url(base_url: str) -> str:
    return f"{base_url}/posts"


@pytest.fixture(scope="class")
def session() -> Iterator[requests.Session]:
    with requests.Session() as requests_session:
        yield requests_session
