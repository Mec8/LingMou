# 🦞 灵眸 Dashboard v2.0

**多 Agent 协调 · Token 统计 · 实时监控**

---

## 🚀 快速开始

```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 启动服务
cd dashboard
python server.py

# 3. 访问 Dashboard
# 浏览器打开：http://localhost:2030
```

---

## ✨ 核心功能

### 1. 📊 概览页面
- 4 个核心指标卡片
- 系统状态实时监控
- 自动刷新（30 秒）

### 2. 🤖 Agent 管理
- Agent 卡片展示
- 工作状态（活跃/空闲）
- 任务统计
- Token 使用
- 成功率

### 3. 💰 Token 统计
- 总消耗图表
- 总费用显示
- 按模型分类明细
- 输入/输出 Token 对比

### 4. 📋 任务管理
- 任务列表表格
- 状态显示（完成/运行/等待）
- 优先级标签
- Agent 分配
- 时间戳

---

## 🎨 设计特点

### 渐变色彩
```css
--primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
--success-gradient: linear-gradient(135deg, #10b981 0%, #059669 100%);
--warning-gradient: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
--danger-gradient: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
```

### 毛玻璃效果
```css
background: rgba(255, 255, 255, 0.95);
backdrop-filter: blur(20px);
```

### 动画效果
- 卡片悬停上浮
- 渐变色彩流动
- 进度条动画
- 页面切换过渡

---

## 📊 API 端点

| 端点 | 方法 | 说明 |
|------|------|------|
| `/` | GET | Dashboard 首页 |
| `/api/stats` | GET | 统计数据 |
| `/api/agents` | GET | Agent 列表 |
| `/api/token/stats` | GET | Token 统计 |
| `/api/tasks` | GET | 任务列表 |
| `/api/health` | GET | 健康检查 |

---

## 🎯 技术栈

**后端：**
- Python 3.10+
- FastAPI
- Uvicorn

**前端：**
- HTML5
- CSS3（渐变 + 动画）
- JavaScript（原生）

**设计：**
- 渐变色彩系统
- 毛玻璃效果
- 响应式布局
- 卡片式设计

---

## 📸 页面预览

### 概览页面
- 4 个统计卡片
- 系统状态区域

### Agent 页面
- Agent 卡片网格
- 状态指示器
- 统计数据

### Token 页面
- 消耗图表
- 费用显示
- 明细表格

### 任务页面
- 任务列表
- 状态标签
- 优先级标识

---

## 🔧 配置说明

### 端口配置
默认端口：2030

修改 `server.py`：
```python
uvicorn.run(app, host="0.0.0.0", port=2030)
```

### 缓存配置
默认缓存时间：60 秒

修改 `server.py`：
```python
CACHE_TTL = 60  # 秒
```

---

## 📈 性能指标

| 指标 | 目标 | 实测 |
|------|------|------|
| 首屏加载 | <0.5 秒 | ~0.3 秒 ✅ |
| API 响应 | <200ms | ~50ms ✅ |
| 页面切换 | <0.3 秒 | ~0.1 秒 ✅ |
| 自动刷新 | 30 秒 | 30 秒 ✅ |

---

## 🎨 配色方案

### 主色调
- 紫色渐变：#667eea → #764ba2
- 粉色渐变：#f093fb

### 功能色
- 成功：#10b981
- 警告：#f59e0b
- 危险：#ef4444
- 信息：#3b82f6

### 中性色
- 文字：#2d3748, #4a5568, #718096
- 背景：rgba(255, 255, 255, 0.95)

---

## 📝 更新日志

### v2.0.0 (2026-03-26)
**全新重构**
- ✅ 渐变彩色 UI
- ✅ 4 个核心页面
- ✅ Agent 管理
- ✅ Token 统计
- ✅ 任务管理
- ✅ 实时刷新

### v1.0.0 (2026-03-26)
**初始版本**
- ✅ 基础 Dashboard
- ✅ 简单统计

---

## 🤝 贡献指南

1. Fork 本仓库
2. 创建特性分支
3. 提交更改
4. 推送到分支
5. 开启 Pull Request

---

## 📄 许可证

MIT License

---

## 📞 联系方式

- **GitHub:** https://github.com/Mec8/LingMou
- **Issues:** https://github.com/Mec8/LingMou/issues

---

**灵眸 · 实时监控 · 智能分析 · 一目了然** ✨
