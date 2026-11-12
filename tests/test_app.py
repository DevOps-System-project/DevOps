"""Automated tests for the service information page.

Run from the repository root with:  python -m pytest -v
"""

import pytest

from app.main import SERVICE_HOURS, SERVICE_NAME, SUPPORT_EMAIL, VERSION, app


@pytest.fixture
def client():
    """Give each test a fake browser that talks to the app without a real server."""
    app.config["TESTING"] = True
    with app.test_client() as test_client:
        yield test_client


# Test 1 - normal output: the main page shows all the required information.
def test_home_page_shows_service_information(client):
    response = client.get("/")
    page = response.get_data(as_text=True)

    assert response.status_code == 200
    assert SERVICE_NAME in page
    assert SUPPORT_EMAIL in page
    assert SERVICE_HOURS in page
    assert f"Version: {VERSION}" in page


# Test 2 - /health: returns 200 and a clear success message.
def test_health_endpoint_returns_ok(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.is_json
    assert response.get_json() == {"status": "ok"}


# Test 3 - error case: a page that does not exist must return 404, not crash.
def test_unknown_page_returns_404(client):
    response = client.get("/this-page-does-not-exist")

    assert response.status_code == 404


# Test 4 - edge case: /health only accepts GET; a POST must be refused (405).
def test_health_rejects_post(client):
    response = client.post("/health")

    assert response.status_code == 405


# Test 5 - the version follows the MAJOR.MINOR.PATCH format used for releases.
def test_version_format():
    parts = VERSION.split(".")

    assert len(parts) == 3
    assert all(part.isdigit() for part in parts)
