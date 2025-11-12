from fastapi import FastAPI, Request
from agent_orchestrator import handle_prompt

app = FastAPI(
    title="AI Hackathon Intelligence Backend",
    description="Agentic Orchestrator + RAG + LLM",
    version="1.0"
)

@app.post("/analyze")
async def analyze(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "")
    result = handle_prompt(prompt)
    return {"response": result}

@app.get("/")
def root():
    return {"message": "Backend is running... use /analyze to send prompts."}
