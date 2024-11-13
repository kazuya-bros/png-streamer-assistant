from enum import Enum
from threading import Lock

class SystemState(str, Enum):
    """システムの状態"""
    STOP = "停止中"
    IDLE = "待機中"
    PAUSE = "一時停止中"
    AI_TALK = "AI対話中"
    AUTO_PILOT = "自動操縦中"

class StateManager:
    """シンプルな状態管理"""
    def __init__(self):
        self._lock = Lock()
        self.state = SystemState.STOP
    
    def set_state(self, new_state: SystemState):
        with self._lock:
            self.state = new_state
    
    def get_state(self) -> SystemState:
        with self._lock:
            return self.state

# グローバルなインスタンス
state_manager = StateManager()