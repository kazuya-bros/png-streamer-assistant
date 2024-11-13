from fastapi import APIRouter
from pydantic import BaseModel
from typing import Dict, Literal

# プロジェクト内のモジュール参照
from app.core.state import SystemState, state_manager
from app.infra.api.models import SystemResponse

router = APIRouter(prefix="/system", tags=["system"])

@router.post(
    "/start",
    response_model=SystemResponse,
    summary="システムを開始",
    description="システムを開始し、IDLEモードに遷移します"
)
async def start_system():
    state_manager.set_state(SystemState.IDLE)
    return SystemResponse(
        status="success",
        state=SystemState.IDLE,
        message="システムを開始しました"
    )

@router.post(
    "/stop",
    response_model=SystemResponse,
    summary="システムを停止",
    description="システムを停止し、STOPモードに遷移します"
)
async def stop_system():
    state_manager.set_state(SystemState.STOP)
    return SystemResponse(
        status="success",
        state=SystemState.STOP,
        message="システムを停止しました"
    )

@router.post(
    "/pause",
    response_model=SystemResponse,
    summary="システムを一時停止",
    description="システムを一時停止します。実行中の処理は継続されます"
)
async def pause_system():
    state_manager.set_state(SystemState.PAUSE)
    return SystemResponse(
        status="success",
        state=SystemState.PAUSE,
        message="システムを一時停止しました"
    )

@router.post(
    "/resume",
    response_model=SystemResponse,
    summary="システムを再開",
    description="一時停止中のシステムを再開します"
)
async def resume_system():
    state_manager.set_state(SystemState.IDLE)
    return SystemResponse(
        status="success",
        state=SystemState.IDLE,
        message="システムを再開しました"
    )
