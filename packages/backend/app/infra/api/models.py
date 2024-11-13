from pydantic import BaseModel
from typing import Dict, Literal
from app.core.state import SystemState

class SystemResponse(BaseModel):
    """システム操作の基本レスポンス"""
    status: Literal["success", "error"]
    state: SystemState
    message: str