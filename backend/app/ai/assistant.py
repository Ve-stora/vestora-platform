import openai
from app.core.config import settings

openai.api_key = settings.OPENAI_API_KEY

SYSTEM_PROMPT = """You are a friendly and knowledgeable financial assistant for the 
Uganda Securities Exchange (USE). You help ordinary Ugandan citizens understand 
capital markets, stock prices, dividends, and investment concepts. 
Always explain things simply, use local context where possible, and avoid jargon.
Answer concisely and helpfully."""

async def ask_assistant(question: str, context: str = "") -> str:
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    if context:
        messages.append({"role": "user", "content": f"Context: {context}"})
    messages.append({"role": "user", "content": question})

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        max_tokens=500,
        temperature=0.7,
    )
    return response.choices[0].message.content
