from typing import Any

import pytest
import requests

REQUIRED_KEYS = {"userId", "id", "title", "body"}
DEFAULT_TIMEOUT = 10


class TestPosts:
    def test_get_posts_list(
        self, session: requests.Session, posts_url: str
    ) -> None:
        response = session.get(posts_url, timeout=DEFAULT_TIMEOUT)

        assert response.status_code == 200

        payload = response.json()
        assert isinstance(payload, list)
        assert payload, "posts list should not be empty"
        assert REQUIRED_KEYS.issubset(payload[0].keys())

    @pytest.mark.parametrize("post_id", [1, 2, 3])
    def test_get_post_by_id(
        self, session: requests.Session, posts_url: str, post_id: int
    ) -> None:
        response = session.get(f"{posts_url}/{post_id}", timeout=DEFAULT_TIMEOUT)

        assert response.status_code == 200

        payload = response.json()
        assert REQUIRED_KEYS.issubset(payload.keys())
        assert payload["id"] == post_id

    @pytest.mark.parametrize(
        "payload",
        [
            {"title": "alpha", "body": "first", "userId": 1},
            {"title": "beta", "body": "second", "userId": 2},
        ],
    )
    def test_create_post(
        self,
        session: requests.Session,
        posts_url: str,
        payload: dict[str, Any],
    ) -> None:
        response = session.post(posts_url, json=payload, timeout=DEFAULT_TIMEOUT)

        assert response.status_code == 201

        data = response.json()
        assert REQUIRED_KEYS.issubset(data.keys())
        assert data["title"] == payload["title"]
        assert data["body"] == payload["body"]
        assert data["userId"] == payload["userId"]

    @pytest.mark.parametrize(
        "post_id, payload",
        [
            (1, {"title": "updated", "body": "content", "userId": 1}),
            (2, {"title": "revised", "body": "text", "userId": 2}),
        ],
    )
    def test_update_post(
        self,
        session: requests.Session,
        posts_url: str,
        post_id: int,
        payload: dict[str, Any],
    ) -> None:
        response = session.put(
            f"{posts_url}/{post_id}",
            json=payload,
            timeout=DEFAULT_TIMEOUT,
        )

        assert response.status_code == 200

        data = response.json()
        assert REQUIRED_KEYS.issubset(data.keys())
        assert data["id"] == post_id
        assert data["title"] == payload["title"]
        assert data["body"] == payload["body"]
        assert data["userId"] == payload["userId"]

    def test_delete_post(self, session: requests.Session, posts_url: str) -> None:
        response = session.delete(f"{posts_url}/1", timeout=DEFAULT_TIMEOUT)

        assert response.status_code == 200

    def test_get_nonexistent_post(
        self, session: requests.Session, posts_url: str
    ) -> None:
        response = session.get(f"{posts_url}/0", timeout=DEFAULT_TIMEOUT)

        assert response.status_code == 404

        payload = response.json()
        assert payload == {}
