import asyncio
import ships_etl


async def main():
    await ships_etl.load_data_to_csv()


if __name__ == "__main__":
    asyncio.run(main())
