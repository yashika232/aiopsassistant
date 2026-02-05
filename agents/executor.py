import asyncio
from tools.github_tool import search_github
from tools.weather_tool import get_weather

TOOL_REGISTRY = {
    "github_search": search_github,
    "weather_fetch": get_weather
}

async def run_tool(action, params):
    tool = TOOL_REGISTRY.get(action)
    if not tool:
        return {"error": f"Unknown action: {action}"}

    try:
        return tool(**params)
    except Exception as e:
        return {"error": str(e)}

def execute(plan: dict):
    async def runner():
        tasks = [
            run_tool(step["action"], step.get("params", {}))
            for step in plan.get("steps", [])
        ]
        return await asyncio.gather(*tasks)

    return asyncio.run(runner())
