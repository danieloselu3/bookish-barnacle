from rag_engine import retrieve_context
from llm_interface import run_llm
from prompt_templates import format_prompt

def handle_prompt(prompt: str):
    """Main orchestration logic connecting RAG and LLM."""
    context = retrieve_context(prompt)
    full_prompt = format_prompt(prompt, context)
    response = run_llm(full_prompt)
    return response
