import config
from .ships_transform import transform_ships_data



async def load_data_to_csv():
    df_ships = await transform_ships_data()
    df_ships.to_csv("ships_data.csv", index=False)  
    config.logger.info("Data saved to CSV successfully.")
