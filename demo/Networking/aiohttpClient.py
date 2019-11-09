import aiohttp
import asyncio


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://localhost:8080') as resp:
            print(resp.status)
            print(await resp.text())


if __name__ == "__main__":
    asyncio.run(main())
