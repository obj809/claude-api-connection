# How to Guide: Claude API Connection

## Description

A Python quickstart guide for getting started with the Anthropic Claude API.

## Requirements

- Python 3.10+
- An Anthropic API key

## main.py

```python
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
```

## Build Steps


1) Create an Anthropic account
[https://platform.claude.com/dashboard](https://platform.claude.com/dashboard)


2) Create an Anthropic API key
Once logged in:
[https://console.anthropic.com/settings/keys](https://console.anthropic.com/settings/keys)


3) Clone this repo
```bash
git clone https://github.com/obj809/claude-api-connection
```
```bash
cd claude-api-connection
```


4) Create a virtual environment
```bash
python -m venv venv
```


5) Activate the virtual environment
macOS / Linux
```bash
source venv/bin/activate
```
Windows (PowerShell)
```powershell
venv\Scripts\Activate.ps1
```


6) Install requirements
```bash
pip install -r requirements.txt
```

Minimum dependencies:
```bash
pip install anthropic python-dotenv
```


7) Create a .env file in the project root
```env
ANTHROPIC_API_KEY=your_api_key_here
```


8) Run main.py
```bash
python main.py
```


## Links

- [Anthropic Claude Models](https://platform.claude.com/docs/en/about-claude/models/overview)

- [Claude API Quickstart](https://platform.claude.com/docs/en/get-started#python)