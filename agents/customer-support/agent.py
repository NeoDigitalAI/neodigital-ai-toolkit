"""
NeoDigital AI Customer Support Agent
Free starter template — customize for your business.
Full implementation: https://neodigital.tech/services/custom-ai-agent-systems
"""

from openai import OpenAI
import json

client = OpenAI()

SYSTEM_PROMPT = """You are a helpful customer support AI agent.
You speak multiple languages and escalate complex issues to humans.
Always be professional, concise, and solution-focused."""

def handle_message(user_message: str, history: list = []) -> str:
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    messages.extend(history)
    messages.append({"role": "user", "content": user_message})
    
    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages,
        temperature=0.7,
        max_tokens=500
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    print("NeoDigital AI Support Agent — neodigital.tech")
    print("Type 'quit' to exit\n")
    history = []
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break
        response = handle_message(user_input, history)
        print(f"Agent: {response}\n")
        history.append({"role": "user", "content": user_input})
        history.append({"role": "assistant", "content": response})
