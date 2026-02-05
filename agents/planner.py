import json
from llm.client import call_llm

PLANNER_PROMPT = """
You are a Planner Agent.

Convert the user task into an ordered execution plan.
Return ONLY valid JSON.

Schema:
{
  "steps": [
    {
      "id": number,
      "action": "github_search | weather_fetch",
      "params": {}
    }
  ]
}
"""

def plan(task: str) -> dict:
    output = call_llm(PLANNER_PROMPT, task)
    return json.loads(output)
