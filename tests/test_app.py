import pytest
from app import app, db


@pytest.fixture
def client():
    """Создаёт тестовый клиент и чистую БД"""
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()


def test_get_todos_empty(client):
    """Пустой список задач"""
    response = client.get('/todos')
    assert response.status_code == 200
    assert response.get_json() == []


def test_create_todo(client):
    """Создание задачи"""
    response = client.post(
        '/todos',
        json={'task': 'изучить CI/CD'},
        content_type='application/json'
    )
    assert response.status_code == 201
    data = response.get_json()
    assert data['task'] == 'изучить CI/CD'
    assert 'id' in data


def test_create_and_get(client):
    """Создаём и получаем список"""
    client.post('/todos', json={'task': 'задача 1'})
    client.post('/todos', json={'task': 'задача 2'})
    
    response = client.get('/todos')
    data = response.get_json()
    
    assert len(data) == 2
    assert data[0]['task'] == 'задача 1'
    assert data[1]['task'] == 'задача 2'


def test_empty_task(client):
    """Пустая задача не должна приниматься"""
    response = client.post(
        '/todos',
        json={'task': ''},
        content_type='application/json'
    )
    assert response.status_code == 201