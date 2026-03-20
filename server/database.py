from contextlib import asynccontextmanager
from fastapi import FastAPI,Request
import asyncpg
from typing import AsyncGenerator
import os

from init_db import create_tables_and_views

DB_URL=os.getenv('DATABASE_URL')

async def get_db_connection(request: Request) -> AsyncGenerator[asyncpg.Connection, None]:
    async with request.app.state.pool.acquire() as connection:
        yield connection

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.pool = await asyncpg.create_pool(DB_URL)
    await create_tables_and_views(app.state.pool)
    
    yield
    
    await app.state.pool.close()
