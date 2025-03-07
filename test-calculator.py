import unittest
from app import app

class TestCalculator(unittest.TestCase):
    

    def setUp(self):
        self.app = app.test_client()

    def test_addition(self):
        # Send a GET request to the endpoint
        response = self.app.get('/add?num1=5&num2=3')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["result"], 8)

    def test_subtraction(self):
        # Send a GET request to the endpoint
        response = self.app.get('/subtract?num1=10&num2=4')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["result"], 6)

    def test_multiplication(self):
        # Send a GET request to the endpoint
        response = self.app.get('/multiply?num1=7&num2=6')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["result"], 42)

    def test_division(self):
        # Send a GET request to the endpoint
        response = self.app.get('/divide?num1=20&num2=5')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["result"], 4)

    def test_division_by_zero(self):
        # Send a GET request to the endpoint
        response = self.app.get('/divide?num1=10&num2=0')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json()["error"], "Division by zero is not allowed")

if __name__ == '__main__':
    unittest.main()