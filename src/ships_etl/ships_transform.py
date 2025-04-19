import pandas as pd
from .ships_extract import get_ships_data
import config


async def transform_ships_data():
    data = await get_ships_data()
    parsed_data = [
        {
            "id": item["id"],
            "legacy_id": item["legacy_id"],
            "type": item["type"],
            "roles": item["roles"],
            "imo": item["imo"],
            "mmsi": item["mmsi"],
            "abs": item["abs"],
            "class": item["class"],
            "mass_kg": item["mass_kg"],
            "mass_lbs": item["mass_lbs"],
            "year_built": item["year_built"],
            "home_port": item["home_port"],
        }
        for item in data
    ]
    df_ships = pd.DataFrame(parsed_data).sort_values(
        by="year_built", ascending=False)

    print(df_ships.head())

    config.logger.info("Transformed ships data successfully.")

    return df_ships
