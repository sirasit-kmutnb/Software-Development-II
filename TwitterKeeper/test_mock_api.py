import unittest
from unittest.mock import patch, Mock
import requests

def get_users():
    """Get list of users"""
    USERS_URL = 'http://jsonplaceholder.typicode.com/users'
    response = requests.get(USERS_URL)
    if response.ok:
        return response
    else:
        return None

class BasicTests(unittest.TestCase):
    # ... other tests
    def test_mock_whole_function(self):
        """Mocking a whole function"""
        mock_get_patcher = patch('requests.get')
        users = [{
            "id": 0,
            "first_name": "Dell",
            "last_name": "Norval",
            "phone": "994-979-3976"
        }]

        # Start patching 'requests.get'.
        mock_get = mock_get_patcher.start()

        # Configure the mock to return a response with status code 200 and a list of users.
        mock_get.return_value = Mock(status_code = 200)
        mock_get.return_value.json.return_value = users

        # Call the service, which will send a request to the server.
        response = get_users()

        # Stop patching 'requests'.
        mock_get_patcher.stop()

        # Assert that the request-response cycle completed successfully.
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), users)


if __name__ == "__main__":
    unittest.main()

# class BasicTests(unittest.TestCase):
#     @patch('requests.get')  # Mock 'requests' module 'get' method.
#     def test_request_response_with_decorator(self, mock_get):
#         """Mocking using a decorator"""
#         mock_get.return_value.status_code = 200 # Mock status code of response.
#         response = get_users()

#         # Assert that the request-response cycle completed successfully.
#         self.assertEqual(response.status_code, 200)


# if __name__ == "__main__":
#     unittest.main()