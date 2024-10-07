import requests
import unittest

class TestPokemonAPI(unittest.TestCase):
    BASE_URL = "https://pokeapi.co/api/v2/pokemon/bulbasaur" 

    def test_status_code(self):
        """Test that the response status code is 200."""
        response = requests.get(self.BASE_URL)
        self.assertEqual(response.status_code, 200, "Status code is not 200")

    def test_response_time(self):
        """Test that the response time is less than 200ms."""
        response = requests.get(self.BASE_URL)
        self.assertLess(response.elapsed.total_seconds() * 1000, 200, "Response time is greater than 200ms")

    def test_response_structure(self):
        """Test that the response has the correct structure."""
        response = requests.get(self.BASE_URL)
        json_data = response.json()
        
        # Check for required properties in the JSON response
        self.assertIn("abilities", json_data, "Response does not have property 'abilities'")
        self.assertIn("id", json_data, "Response does not have property 'id'")
        self.assertIn("name", json_data, "Response does not have property 'name'")

    def test_pokemon_name(self):
        """Test that the Pokemon name is 'bulbasaur'."""
        response = requests.get(self.BASE_URL)
        json_data = response.json()
        self.assertEqual(json_data['name'], 'bulbasaur', "Pokemon name is not 'bulbasaur'")

if __name__ == "__main__":
    unittest.main()

