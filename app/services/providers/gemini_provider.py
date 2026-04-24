import httpx
import os

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

async def generate(prompt: str):
    async with httpx.AsyncClient() as client:
        res = await client.post(
            f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={GEMINI_API_KEY}",
            json={
                "contents": [
                    {
                        "parts": [{"text": prompt}]
                    }
                ]
            }
        )
        return res.json()