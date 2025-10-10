from app import app

def test_home_route():
    """Ensure the Flask app home route responds successfully."""
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Mortality" in response.data or b"Dashboard" in response.data
