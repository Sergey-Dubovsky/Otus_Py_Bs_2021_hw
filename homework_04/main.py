"""
Домашнее задание №3
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""

import asyncio
# from jsonplaceholder_requests import fetch_users_data, fetch_posts_data

from aiohttp import ClientSession

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"

async def fetch_json(session: ClientSession, url: str) -> dict:
    async with session.get(url) as response:
        return await response.json()

async def fetch_users_data() -> dict:
    async with ClientSession() as session:
        return await fetch_json(session, USERS_DATA_URL)

async def fetch_posts_data() -> dict:
    async with ClientSession() as session:
        return await fetch_json(session, POSTS_DATA_URL)

async def async_main():


    users_data, posts_data = await asyncio.gather(
        fetch_users_data(),
        fetch_posts_data(),
    )
    # print (users_data)
    print (posts_data)

if __name__ == '__main__':
    asyncio.run(async_main())
    