import config
from base_extractor import fetch_data


async def get_ships_data():
    data = await fetch_data(config.ENDPOINTS["ships"])
    config.logger.info("Fetched ships data successfully.")
    return data