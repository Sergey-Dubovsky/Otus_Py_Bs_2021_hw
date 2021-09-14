import asyncio
from jsonplaceholder_requests import fetch_users_data, fetch_posts_data
from models import Base,User,Post,engine,session

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        print("Created tables")

async def create_users(user_data):
    async with session() as sess:
        async with sess.begin():
            for user in user_data:
                sess.add(
                    User(
                        id=user['id'], 
                        name=user['name'], 
                        username=user['username'], 
                        email=user['email']
                        )
                    )


async def create_posts(post_data):
    async with session() as sess:
        async with sess.begin():
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
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(async_main())
    