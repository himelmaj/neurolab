from fastapi_pagination import Page
from fastapi import Query, FastAPI
import logging
from collections.abc import AsyncIterator, Callable, Sequence
from contextlib import AbstractAsyncContextManager
from .database import init_db, close_db_connection
from contextlib import asynccontextmanager, AsyncExitStack

Page = Page.with_custom_options(
    size=Query(10, ge=1, le=50),
) 

async def common_parameters(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def startup(app: FastAPI):
    logger.info("Starting up the application...")
    init_db()
    yield
    logger.info("Application startup complete.")

@asynccontextmanager
async def shutdown(app: FastAPI):
    logger.info("Shutting down the application...")
    close_db_connection()
    yield
    logger.info("Application shutdown complete.")
    
@asynccontextmanager
async def _manager(app: FastAPI, lifespans: Sequence[Callable[[FastAPI], AbstractAsyncContextManager[None]]]) -> AsyncIterator[None]:
    exit_stack = AsyncExitStack()
    async with exit_stack:
        for lifespan in lifespans:
            await exit_stack.enter_async_context(lifespan(app))
        yield

class Lifespans:
    def __init__(self, lifespans: Sequence[Callable[[FastAPI], AbstractAsyncContextManager[None]]],) -> None:
        self.lifespans = lifespans

    def __call__(self, app: FastAPI) -> AbstractAsyncContextManager[None]:
        self.app = app
        return _manager(app, lifespans=self.lifespans)