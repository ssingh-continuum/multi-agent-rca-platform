from fastapi import FastAPI
from pydantic import BaseModel

from graph.workflow import workflow


app = FastAPI()


class IncidentRequest(BaseModel):

    description: str


@app.get("/health")
@app.get("/health")
def health():

    return {
        "status": "UP",
        "llm": "qwen3:8b",
        "vector_store": "chromadb"
    }


@app.post("/analyze")
def analyze(
    req: IncidentRequest
):

    result = workflow.invoke({
        "incident": req.description,
        "logs":"",
        "history":"",
        "rca":""
    })

    return {
        "incident": req.description,
        "logs": result["logs"],
        "metrics": result["metrics"],
        "historical_context": result["history"],
        "rca": result["rca"],
        "recommendation": result["recommendation"]
    }
