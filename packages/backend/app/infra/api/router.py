from fastapi import APIRouter
from .routes import system, mode, program, talk, memory

# APIルーターの初期化
api_router = APIRouter(prefix="/api")

# 各機能のルーターを登録
api_router.include_router(system.router)
# api_router.include_router(mode.router)
# api_router.include_router(program.router)
# api_router.include_router(talk.router)
# api_router.include_router(memory.router)