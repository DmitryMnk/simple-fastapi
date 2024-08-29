from contextlib import asynccontextmanager

import uvicorn
from sqlalchemy.testing.plugin.plugin_base import logging

from core.config import settings
from core.models import db_helper, Base
from fastapi import FastAPI
import logging
from api_v1 import router as router_v1

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    #     await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(router=router_v1, prefix=settings.api_v1_prefix)




@app.get('/')
async def main_page():

    return {
        'message': 'так держать'
    }

if __name__ == '__main__':
    uvicorn.run("main:app", port=8010, reload=True)
