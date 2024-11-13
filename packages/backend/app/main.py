import os
import asyncio

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

# プロジェクト内のモジュール参照
from app.infra.api.router import api_router
from app.core.state import state_manager

# .envファイルの読み込み
load_dotenv()

# メインループタスクの参照を保持
main_loop_task = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    """アプリケーションのライフサイクル管理"""
    # 起動時の処理
    global main_loop_task
    main_loop_task = asyncio.create_task(main_loop())
    print("アプリケーションが起動しました")
    
    yield  # アプリケーションの実行中
    
    # 終了時の処理
    if main_loop_task:
        main_loop_task.cancel()
        try:
            await main_loop_task
        except asyncio.CancelledError:
            pass
    print("アプリケーションを終了します")

# アプリケーションの初期化
app = FastAPI(
    title="PNG Streamer Assistant",
    description="表情差分だけで使える実況者向けAIアシスタントシステム",
    version="0.1.0",
    lifespan=lifespan
)

# CORS設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("CORS_ORIGINS", "*").split(","),  # 環境変数から読み込み
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# APIルーターの登録
app.include_router(api_router)

async def main_loop():
    """メインループ（状態監視）"""
    while True:
        current_state = state_manager.get_state()
        print(f"システムの状態: {current_state}")
        await asyncio.sleep(1)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app, 
        host=os.getenv("HOST", "0.0.0.0"),
        port=int(os.getenv("PORT", 8000))
    )
