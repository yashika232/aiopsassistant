from llm.client import call_llm

VERIFIER_PROMPT = """
You are a Verifier Agent.

Check whether the task is fully answered.
Fix missing information if possible.
Return a clear, structured final response.
"""

def verify(task: str, results):
    prompt = f"""
Task:
{task}

Execution Results:
{results}

Produce the final answer.
"""
    return call_llm(VERIFIER_PROMPT, prompt)
