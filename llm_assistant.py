import re
import json
import time
from typing import Tuple
from ollama import Client, ChatResponse

client = Client(host="http://host.docker.internal:11434")

SYSTEM_PROMPT = """
You are a Python code generation assistant.
When given a user prompt, respond **only** with a **single-line JSON** object (no pretty-print, no literal newlines).
Make sure:
1) Field "title": short English title, max 7 words.
2) Field "code": a Python code string where **all** line breaks are escaped as '\\n'. 
Example:
{"title":"Example","code":"```python\\nprint('Hi')\\n```"}
"""

def _extract_json_block(text: str) -> str:

    match = re.search(r"\{.*\}", text, re.DOTALL)
    if not match:
        raise ValueError("Json not found.")
    block = match.group(0)
    
    block = block.replace("\r\n", "\\n").replace("\n", "\\n")
    return block

def generate_code(
    user_prompt: str,
    model: str = "llama3.2",
    retries: int = 3,
    backoff_factor: float = 1.0
) -> Tuple[str, str]:

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user",   "content": user_prompt}
    ]
    last_exc = None

    for attempt in range(1, retries + 1):
        try:
            resp: ChatResponse = client.chat(model=model, messages=messages)
            raw = resp.message.content.strip()

            json_block = _extract_json_block(raw)
            data = json.loads(json_block)

            title = data.get("title", "").strip()
            code  = data.get("code", "").strip()
            return title, code

        except Exception as e:
            last_exc = e
            wait = backoff_factor * (2 ** (attempt - 1))
            print(f"[Attempt {attempt} failed: {e!r}] - retrying in {wait}s")
            time.sleep(wait)

    raise RuntimeError(f"generate_code failed ({retries} deneme): {last_exc}")

if __name__ == "__main__":
    prompt = "Write a Python function that returns the factorial of a number."
    title, code = generate_code(prompt)
