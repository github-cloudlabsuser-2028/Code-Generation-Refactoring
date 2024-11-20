import unittest
from unittest.mock import patch
from api import get_weather

class TestGetWeather(unittest.TestCase):

    @patch('api.requests.get')
    def test_get_weather_valid_city(self, mock_get):
        mock_response = {
            'name': 'London',
            'main': {'temp': 15},
            'weather': [{'description': 'clear sky'}]
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        result = get_weather('London', 'fake_api_key')
        self.assertEqual(result['city'], 'London')
        self.assertEqual(result['temperature'], 15)
        self.assertEqual(result['description'], 'clear sky')

    @patch('api.requests.get')
    def test_get_weather_invalid_city(self, mock_get):
        mock_get.return_value.status_code = 404

        result = get_weather('InvalidCity', 'fake_api_key')
        self.assertIsNone(result)

    @patch('api.requests.get')
    def test_get_weather_empty_city(self, mock_get):
        mock_get.return_value.status_code = 404

        result = get_weather('', 'fake_api_key')
        self.assertIsNone(result)

    @patch('api.requests.get')
    def test_get_weather_valid_city_different_temp(self, mock_get):
        mock_response = {
            'name': 'New York',
            'main': {'temp': 20},
            'weather': [{'description': 'few clouds'}]
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        result = get_weather('New York', 'fake_api_key')
        self.assertEqual(result['city'], 'New York')
        self.assertEqual(result['temperature'], 20)
        self.assertEqual(result['description'], 'few clouds')

    @patch('api.requests.get')
    def test_get_weather_valid_city_different_description(self, mock_get):
        mock_response = {
            'name': 'Tokyo',
            'main': {'temp': 25},
            'weather': [{'description': 'rain'}]
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        result = get_weather('Tokyo', 'fake_api_key')
        self.assertEqual(result['city'], 'Tokyo')
        self.assertEqual(result['temperature'], 25)
        self.assertEqual(result['description'], 'rain')

if __name__ == '__main__':
    unittest.main()