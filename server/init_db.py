import asyncpg
from .Queries.tables import * 

async def create_tables_and_views(pool: asyncpg.Pool):
    async with pool.acquire() as connection:
        await connection.execute(CREATE_TASK_TABLE)