import aiohttp
from config.logging_config import logger


async def fetch_data(url: str) -> list:
    try:
        logger.info(f"Fetching data from {url}")
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()
                return await response.json()
    except aiohttp.ClientError as e:
        logger.error(f"Error fetching data from {url}: {e}")
        return []
