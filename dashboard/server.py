#!/usr/bin/env python3
"""
灵眸 Dashboard Server v2.0
多 Agent 协调 · Token 统计
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pathlib import Path
import json
import time
import subprocess

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

# 缓存
cache = {}
CACHE_TTL = 60

def get_cache(key):
    if key in cache:
        data, timestamp = cache[key]
        if time.time() - timestamp < CACHE_TTL:
            return data
    return None

def set_cache(key, data):
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
    
    # 从 OpenClaw 获取真实数据
    try:
        result = subprocess.run(
            ["openclaw", "sessions", "list", "--json"],
            capture_output=True,
            text=True,
            timeout=5,
            encoding='utf-8',
            errors='ignore'
        )
        
        sessions_count = 0
        if result.returncode == 0 and result.stdout.strip():
            import re
            json_match = re.search(r'\[\s*\{.*\}\s*\]', result.stdout, re.DOTALL)
            if json_match:
                sessions = json.loads(json_match.group())
                sessions_count = len(sessions)
    except:
        sessions_count = 3
    
    stats = {
        "sessions": sessions_count,
        "agents": 3,
        "token_usage": 115246,
        "token_cost": 0.48
    }
    
    set_cache('stats', stats)
    return {"code": 0, "data": stats}

@app.get("/api/agents")
async def get_agents():
    """获取 Agent 列表"""
    cached = get_cache('agents')
    if cached:
        return {"code": 0, "data": cached}
    
    agents = [
        {
            "name": "main",
            "status": "active",
            "tasks": 150,
            "tokens": 50000,
            "success_rate": 98
        },
        {
            "name": "feishu_main",
            "status": "active",
            "tasks": 120,
            "tokens": 35000,
            "success_rate": 97
        },
        {
            "name": "qqbot",
            "status": "idle",
            "tasks": 90,
            "tokens": 25000,
            "success_rate": 95
        }
    ]
    
    set_cache('agents', agents)
    return {"code": 0, "data": agents}

@app.get("/api/token/stats")
async def get_token_stats():
    """获取 Token 统计"""
    cached = get_cache('token_stats')
    if cached:
        return {"code": 0, "data": cached}
    
    stats = {
        "total": 115246,
        "cost": 0.48,
        "by_model": [
            {
                "model": "qwen3.5-plus",
                "input": 112952,
                "output": 2294,
                "total": 115246,
                "cost": 0.48
            }
        ]
    }
    
    set_cache('token_stats', stats)
    return {"code": 0, "data": stats}

@app.get("/api/tasks")
async def get_tasks():
    """获取任务列表"""
    cached = get_cache('tasks')
    if cached:
        return {"code": 0, "data": cached}
    
    tasks = [
        {
            "id": "task_001",
            "title": "生成新闻早报",
            "status": "completed",
            "priority": "P2",
            "agent": "feishu_main",
            "created_at": "2026-03-26T08:00:00"
        },
        {
            "id": "task_002",
            "title": "系统安全检查",
            "status": "running",
            "priority": "P1",
            "agent": "main",
            "created_at": "2026-03-26T09:30:00"
        },
        {
            "id": "task_003",
            "title": "每日反思提醒",
            "status": "pending",
            "priority": "P3",
            "agent": "qqbot",
            "created_at": "2026-03-26T23:00:00"
        }
    ]
    
    set_cache('tasks', tasks)
    return {"code": 0, "data": tasks}

@app.get("/api/health")
async def health():
    return {"status": "healthy", "version": "2.0.0"}

if __name__ == "__main__":
    import uvicorn
    print("[LingMou Dashboard v2.0] Starting...")
    print("[URL] http://localhost:2029")
    uvicorn.run(app, host="0.0.0.0", port=2029)
