from tools.github_tool import search_github
from tools.weather_tool import get_weather

def execute(plan: dict):
    results = []

    for step in plan["steps"]:
        action = step["action"]
        params = step["params"]

        if action == "github_search":
            results.append(search_github(**params))

        elif action == "weather_fetch":
            results.append(get_weather(**params))

    return results
