import pytest
from app import app

# Test case for the 'hello_world' route
def test_hello_world():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert b'Hello, World!' in response.data

# Test case for the 'add_numbers' route
def test_add_numbers():
    with app.test_client() as client:
        response = client.get('/add/3/4')
        assert response.status_code == 200
        assert b'{"result":7}' in response.data

# Test case for the 'subtract_numbers' route
def test_subtract_numbers():
    with app.test_client() as client:
        response = client.get('/subtract/10/4')
        assert response.status_code == 200
        assert b'{"result":6}' in response.data

# Test case for the 'multiply_numbers' route
def test_multiply_numbers():
    with app.test_client() as client:
        response = client.get('/multiply/3/5')
        assert response.status_code == 200
        assert b'{"result":15}' in response.data

# Test case for the 'divide_numbers' route
def test_divide_numbers():
    with app.test_client() as client:
        response = client.get('/divide/10/2')
        assert response.status_code == 200
        assert b'{"result":5.0}' in response.data

        # Test division by zero
        response = client.get('/divide/10/0')
        assert response.status_code == 400
        assert b'{"error":"Cannot divide by zero"}' in response.data

# Test case for the 'concat_strings' route
def test_concat_strings():
    with app.test_client() as client:
        # Test successful concatenation
        response = client.post('/concat', json={"str1": "Hello", "str2": "World"})
        assert response.status_code == 200
        assert b'{"result":"HelloWorld"}' in response.data

        # Test missing 'str1' or 'str2'
        response = client.post('/concat', json={"str1": "Hello"})
        assert response.status_code == 400
        assert b'{"error":"Both \'str1\' and \'str2\' are required"}' in response.data
