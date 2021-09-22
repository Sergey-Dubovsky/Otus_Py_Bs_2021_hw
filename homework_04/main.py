import asyncio
from functools import wraps
from jsonplaceholder_requests import fetch_users_data, fetch_posts_data
from models import Base,User,Post,engine,Session
from sys import platform 

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        print("Created tables")


def with_session(func):
    @wraps(func)
    async def wrapper(data):
        async with Session() as sess:
            async with sess.begin():
                return await func(sess,data)

    return wrapper

@with_session
async def create_users(sess,user_data):
    for user in user_data:
        sess.add(
            User(
                id=user['id'], 
                name=user['name'], 
                username=user['username'], 
                email=user['email']
                )
            )

@with_session
async def create_posts(sess,post_data):
    for post in post_data:
        sess.add(
            Post(
                id=post['id'], 
                title=post['title'], 
                body=post['body'], 
                user_id=post['userId']
                )
            )


async def async_main():

    await create_tables()

    users_data, posts_data = await asyncio.gather(
        fetch_users_data(),
        fetch_posts_data(),
    )

    await create_users(users_data)
    await create_posts(posts_data)


if __name__ == '__main__':
    
    if platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(async_main())
    