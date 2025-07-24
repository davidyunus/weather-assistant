from simulated_data.mock_data import SIMULATED_WEATHER

class WeatherTool:
    def get_weather(self, city: str) -> dict:
        return SIMULATED_WEATHER.get(city, {"error": "City not found"})
