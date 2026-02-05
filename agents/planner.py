import json
from llm.client import call_llm

# ===== Strict Planner Prompt =====
PLANNER_PROMPT = """
You are a Planner Agent.

Convert the user task into a JSON plan.

RULES:
- Output ONLY valid JSON
- Do NOT include explanations or markdown
- Use ONLY the allowed actions
- Include all required parameters

ALLOWED ACTIONS:
1. github_search
   Required params: query (string), limit (number)
2. weather_fetch
   Required params: city (string)

SCHEMA:
{
  "steps": [
    {
      "id": number,
      "action": "github_search | weather_fetch",
      "params": object
    }
  ]
}
"""

# ===== Hard Constraints =====
ALLOWED_ACTIONS = {"github_search", "weather_fetch"}

REQUIRED_PARAMS = {
    "github_search": {"query", "limit"},
    "weather_fetch": {"city"}
}

# ===== Planner Function =====
def plan(task: str) -> dict:
    raw_output = call_llm(PLANNER_PROMPT, task)

    try:
        # Extract JSON safely
        start = raw_output.find("{")
        end = raw_output.rfind("}") + 1
        if start == -1 or end == -1:
            raise ValueError("No JSON object found in LLM output")

        plan_json = json.loads(raw_output[start:end])

        # Validate structure
        if "steps" not in plan_json or not isinstance(plan_json["steps"], list):
            raise ValueError("Missing or invalid 'steps' array")

        for step in plan_json["steps"]:
            # Required keys
            for key in ("id", "action", "params"):
                if key not in step:
                    raise ValueError(f"Missing key '{key}' in step")

            action = step["action"]
            params = step["params"]

            # Action validation
            if action not in ALLOWED_ACTIONS:
                raise ValueError(f"Invalid action: {action}")

            # Params validation
            if not isinstance(params, dict):
                raise ValueError(f"'params' must be an object for action {action}")

            missing = REQUIRED_PARAMS[action] - params.keys()
            if missing:
                raise ValueError(
                    f"Missing params {missing} for action {action}"
                )

        return plan_json

    except Exception as e:
        return {
            "steps": [],
            "error": f"Planner validation failed: {str(e)}"
        }
