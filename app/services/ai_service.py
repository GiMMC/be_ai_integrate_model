from app.services.providers import openai_provider, gemini_provider

async def generate_text(model: str, prompt: str):
    if model == "openai":
        return await openai_provider.generate(prompt)
    
    elif model == "gemini":
        return await gemini_provider.generate(prompt)
    
    else:
        raise ValueError("Unsupported model")