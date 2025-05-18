import httpx

async def make_request(method: str, url: str, jsondata=None,headers=None):
    """Generic function to make API requests"""
    async with httpx.AsyncClient() as client:
        response = await client.request(method, url, json=jsondata, headers=headers, timeout=None)
        return response.json()