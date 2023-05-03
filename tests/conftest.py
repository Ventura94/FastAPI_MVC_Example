import pytest
from starlette.testclient import TestClient

from src.ASGI.app import app


@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"


@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client
