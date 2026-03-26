#!/usr/bin/env python3
"""
灵眸 Dashboard Server v2.0
全新重构 · 简洁高效
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pathlib import Path
import json
import time

app = FastAPI(title="灵眸 Dashboard", version="2.0.0")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 路径
DASHBOARD_DIR = Path(__file__).parent
WORKSPACE = Path.home() / ".openclaw" / "workspace"
DATA_DIR = WORKSPACE / "data" / "lingmou"

# 缓存
cache = {}

def get_cache(key, ttl=60):
    if key in cache:
        data, timestamp = cache[key]
        if time.time() - timestamp < ttl:
            return data
    return None

def set_cache(key, data, ttl=60):
    cache[key] = (data, time.time())

@app.get("/")
async def root():
    return FileResponse(DASHBOARD_DIR / "index.html")

@app.get("/api/stats")
async def get_stats():
    """获取统计数据"""
    cached = get_cache('stats')
    if cached:
        return {"code": 0, "data": cached}
    
    # 模拟数据（后续可以连接真实数据源）
    stats = {
        "sessions": 3,
        "agents": 3,
        "token_usage": 15000,
        "token_cost": 0.30
    }
    
    set_cache('stats', stats)
    return {"code": 0, "data": stats}

@app.get("/api/health")
async def health():
    return {"status": "healthy", "version": "2.0.0"}

if __name__ == "__main__":
    import uvicorn
    print("[LingMou Dashboard v2.0] Starting...")
    print("[URL] http://localhost:2026")
    uvicorn.run(app, host="0.0.0.0", port=2029)
