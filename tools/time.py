from simulated_data.mock_data import SIMULATED_TIME

class TimeTool:
    def get_time(self, city: str) -> str:
        return SIMULATED_TIME.get(city, "Unknown")
