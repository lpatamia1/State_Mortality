from app import app

def test_home_route():
    """Ensure the Flask homepage loads successfully."""
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"State Mortality Dashboard" in response.data
