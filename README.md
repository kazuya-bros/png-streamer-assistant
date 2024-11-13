# png-streamer-assistant

表情差分だけで使える実況者向けAIアシスタントシステム

## プロジェクト構成
```
png-streamer-assistant/
├── packages/
│   ├── backend/               # バックエンドアプリ (Python)
│   │   ├── app/
│   │   │   ├── core/         # ビジネスロジック
│   │   │   │   ├── state/    # 状態管理
│   │   │   │   ├── ai/      # AI対話処理
│   │   │   │   └── handlers/ # 入力ハンドラー
│   │   │   ├── infra/       # インフラ層
│   │   │   │   ├── api/     # REST API
│   │   │   │   │   ├── routes/
│   │   │   │   │   │   ├── system.py
│   │   │   │   │   │   ├── mode.py
│   │   │   │   │   │   ├── program.py
│   │   │   │   │   │   ├── talk.py
│   │   │   │   │   │   └── memory.py
│   │   │   │   │   ├── models.py
│   │   │   │   │   └── router.py
│   │   │   │   ├── websocket/
│   │   │   │   └── database/
│   │   │   └── adapters/    # 外部サービス連携
│   │   │       ├── youtube/
│   │   │       ├── tts/
│   │   │       └── llm/
│   │   ├── tests/           # テストコード
│   │   └── docs/            # APIドキュメント
│   │
│   ├── frontend/            # フロントエンド (Unity)
│   ├── controller/          # コントローラー (Electron)
│   └── voice-recorder/      # 音声録音 (Electron)
│
├── docs/                    # プロジェクト全体のドキュメント
└── tools/                   # 開発ツール
```

各アプリケーションは独立して動作し、以下のような関係性を持ちます：
1.backend
中心的なアプリケーション
WebSocketサーバーとしてフロントエンドと通信
REST APIでその他のアプリと通信
DBアクセスの一元管理
2.frontend
Electron/Unityアプリ
キャラクター表示と制御
WebSocketでバックエンドと通信
3.controller
シンプルなGUIアプリ
ショートカットキーの管理
バックエンドのAPIを呼び出し
4.voice_recorder
音声入力の処理に特化
マイク・ゲーム音声の文字起こし
WebSocketでバックエンドに送信
5.autopilot_manager
自動運転モード専用の管理アプリ
独自のAPIを提供
バックエンドのAPIを利用

## 開発環境のセットアップ

### バックエンド (Python)

#### 必要条件
- Python 3.11以上
- pip

#### セットアップ手順


### バックエンド (Python)

```bash
# パッケージのルートディレクトリに移動
cd packages/backend

# venv作成
python -m venv .venv
# venv有効化 (Linux)
source .venv/bin/activate 
# venv有効化 (Windows)
.venv\Scripts\activate

#  依存関係インストール
pip install -r requirements.txt
pip install -r requirements-dev.txt

# 開発サーバー起動
cd packages/backend
uvicorn app.main:app --reload
```

### フロントエンド (Unity)

Coming soon...

### 設定アプリ (Electron)

Coming soon...

## ドキュメント

backendアプリを起動した状態で以下のURLにアクセスしてください
[API仕様(Swagger)](http://localhost:8000/docs)
[API仕様(ReDoc)](http://localhost:8000/redoc)

- [API仕様](docs/protocol/api/README.md)
- [WebSocket仕様](docs/protocol/websocket/README.md)
- [アーキテクチャ](docs/architecture/README.md)