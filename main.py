from fastapi import FastAPI
from agents.planner import plan
from agents.executor import execute
from agents.verifier import verify

app = FastAPI(title="AI Operations Assistant")

@app.post("/run")
def run_task(task: str):
    plan_json = plan(task)
    results = execute(plan_json)
    final_answer = verify(task, results)

    return {
        "plan": plan_json,
        "results": results,
        "final_answer": final_answer
    }
