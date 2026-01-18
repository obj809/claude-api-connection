# main.py

import os
from dotenv import load_dotenv
import anthropic

load_dotenv()

anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
if not anthropic_api_key:
    raise RuntimeError("ANTHROPIC_API_KEY not set")

MODEL = "claude-sonnet-4-5"
PROMPT = "Write a one-sentence bedtime story about a shadow that wants to dance on its own."

client = anthropic.Anthropic(api_key=anthropic_api_key)

message = client.messages.create(
    model=MODEL,
    max_tokens=128,
    messages=[
        {
            "role": "user",
            "content": PROMPT
        }
    ]
)

print(message.content[0].text if message.content else "")
