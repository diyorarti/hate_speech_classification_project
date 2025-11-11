import httpx
from api.core.config import settings


async def predict(text: str):
    payload = {"inputs": text}
    headers = {
        "Authorization": f"Bearer {settings.HF_TOKEN}",
        "Content-Type": "application/json",
    }

    async with httpx.AsyncClient(timeout=settings.REQUEST_TIMEOUT_SECONDS) as client:
        response = await client.post(
            settings.ENDPOINT_URL,
            headers=headers,
            json=payload
        )

    if response.status_code != 200:
        return {"error": response.text}

    return response.json()
