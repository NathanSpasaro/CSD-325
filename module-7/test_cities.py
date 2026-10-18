# Import Python's unit testing framework and the function being tested.
import unittest
from city_functions import city_country

# Define a test class to verify the city_country function.
class TestCities(unittest.TestCase):
    def test_city_country(self):
        result = city_country("Santiago", "Chile")
        self.assertEqual(result, "Santiago, Chile")

    def test_city_country_population(self):
        result = city_country("Santiago", "Chile", "5000000")
        self.assertEqual(result, "Santiago, Chile - population 5000000")

    def test_city_country_population_language(self):
        result = city_country("Santiago", "Chile", "5000000", "Spanish")
        self.assertEqual(result, "Santiago, Chile - population 5000000, Spanish")