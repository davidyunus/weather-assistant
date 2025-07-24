from simulated_data.mock_data import SIMULATED_FACTS

class CityFactsTool:
    def get_facts(self, city: str) -> dict:
        return SIMULATED_FACTS.get(city, {"error": "City not found"})
