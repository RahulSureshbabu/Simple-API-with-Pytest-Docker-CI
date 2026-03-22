import os
import time
import subprocess

import pytest
import requests

BASE = os.getenv("API_BASE", "http://localhost:3000")

# Moved to option A: assume the API service is started in docker-compose.
# The Windows batch-based server startup fixture is preserved below as comments
# for local dev traceability.

# @pytest.fixture(scope="session", autouse=True)
# def server():
#     """Start the API server from start-server.bat before tests and stop it after."""
#     repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
#     server_script = os.path.join(repo_root, "start-server.bat")
#
#     proc = subprocess.Popen(["cmd", "/c", server_script], cwd=repo_root)
#
#     # wait for the server to be available
#     for _ in range(30):
#         try:
#             r = requests.get(f"{BASE}/hello", timeout=1)
#             if r.status_code == 200:
#                 break
#         except requests.RequestException:
#             time.sleep(1)
#     else:
#         proc.terminate()
#         proc.wait(timeout=5)
#         raise RuntimeError("Server did not start in time")
#
#     yield
#
#     proc.terminate()
#     try:
#         proc.wait(timeout=5)
#     except subprocess.TimeoutExpired:
#         proc.kill()

@pytest.fixture
def api_base():
    """Fixture providing the API base URL."""
    return BASE

@pytest.fixture
def client():
    """Fixture providing a reusable HTTP session for all tests."""
    session = requests.Session()
    yield session
    session.close()

def test_get_hello_status(client, api_base):
    r = client.get(f"{api_base}/hello")
    assert r.status_code == 200

def test_get_hello_json(client, api_base):
    r = client.get(f"{api_base}/hello")
    assert r.headers["Content-Type"].startswith("application/json")

def test_get_hello_message_field(client, api_base):
    r = client.get(f"{api_base}/hello")
    data = r.json()
    assert "message" in data

def test_get_hello_value(client, api_base):
    r = client.get(f"{api_base}/hello")
    data = r.json()
    assert data["message"] == "Hello World!"

def test_put_hello_status(client, api_base):
    r = client.put(f"{api_base}/hello", json={"message": "Test PUT"})
    assert r.status_code == 200

def test_put_hello_updates_message(client, api_base):
    msg = "Updated via test"
    r = client.put(f"{api_base}/hello", json={"message": msg})
    assert r.json()["updated"] == msg

def test_put_missing_message(client, api_base):
    r = client.put(f"{api_base}/hello", json={})
    # This SHOULD be 400, but your API returns 200.
    # Update your API to fix this.
    assert r.status_code == 400

