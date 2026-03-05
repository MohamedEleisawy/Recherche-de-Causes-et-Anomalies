import pytest
from app import app

@pytest.fixture
def client():
    # On configure l'app en mode test
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_route(client):
    # On tape sur la route
    response = client.get('/health')
    
    # On vérifie qu'on a bien un code 200 (OK) et le bon statut
    assert response.status_code == 200
    assert response.json["status"] == "ok"