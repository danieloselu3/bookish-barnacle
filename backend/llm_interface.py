import requests
import json
import os

OLLAMA_URL = os.getenv("OLLAMA_HOST", "http://llm:11434")

def run_llm(prompt: str) -> str:
    """Sends a prompt to the local Ollama LLM and streams the response."""
    payload = {"model": "llama3", "prompt": prompt}
    response = requests.post(f"{OLLAMA_URL}/api/generate", json=payload, stream=True)
    output = ""
    for line in response.iter_lines():
        if line:
            content = json.loads(line)
            output += content.get("response", "")
    return output
