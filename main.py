from fastapi import FastAPI, HTTPException
from agents.planner import plan
from agents.executor import execute
from agents.verifier import verify

app = FastAPI(title="AI Operations Assistant")

@app.post("/run")
def run_task(task: str):
    try:
        # 1. Plan
        plan_json = plan(task)
        if "error" in plan_json:
            raise HTTPException(status_code=400, detail=plan_json["error"])
        
        # 2. Execute
        results = execute(plan_json)
        
        # 3. Verify
        final_answer = verify(task, results)

        return {
            "plan": plan_json,
            "results": results,
            "final_answer": final_answer
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 