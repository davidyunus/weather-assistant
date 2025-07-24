from tools.weather import WeatherTool
from tools.time import TimeTool
from tools.facts import CityFactsTool

class PlanMyCityVisitTool:
    def __init__(self):
        self.weather_tool = WeatherTool()
        self.time_tool = TimeTool()
        self.facts_tool = CityFactsTool()

    def plan_visit(self, city: str) -> dict:
        thinking = f"Thinking: Gathering facts, weather, and time for {city}..."

        facts = self.facts_tool.get_facts(city)
        weather = self.weather_tool.get_weather(city)
        time = self.weather_tool.get_weather(city)

        return {
            "thinking": thinking,
            "city": city,
            "description": facts.get("description", "N/A"),
            "country": facts.get("country", "N/A"),
            "population": facts.get("population", "N/A"),
            "weather": weather,
            "local_time": time
        }
