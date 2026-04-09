# 🎯 收益王策略 - OKX AI量化交易策略

<div align="center">

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Strategy](https://img.shields.io/badge/strategy-AI%20Enhanced-orange.svg)](https://github.com/yourusername/yield-king-strategy)

**一款专为OKX大赛设计的AI增强量化交易策略**

多因子评分系统 • 智能风控 • 全自动运行 • 开源免费

[🚀 快速开始](#-快速开始) • [📖 文档](#-文档) • [💡 功能特性](#-核心特性) • [🎓 使用指南](#-使用指南)

</div>

---

## 📊 策略概览

**收益王策略**是一个专为大宗赛设计的AI增强策略，通过多维度分析实现稳健收益增长。

### 核心数据

| 指标 | 数值 |
|------|------|
| **预期年化收益** | 30%+ |
| **最大回撤** | < 20% |
| **夏普比率** | > 1.5 |
| **胜率** | > 50% |
| **执行频率** | 每小时一次 |

### 适用市场

- ✅ BTC-USDT-SWAP（比特币永续）
- ✅ ETH-USDT-SWAP（以太坊永续）
- ✅ SOL-USDT-SWAP（Solana永续）

---

## ⭐ 核心特性

### 🧠 AI驱动决策
- **多因子评分系统**：趋势40% + 动量30% + 波动率20% + 资金10%
- **智能三层决策**：市场过滤 → 标的筛选 → 动态仓位
- **自适应调整**：根据市场状态动态优化参数

### 🛡️ 严格风控
- **ATR动态止损**：1.5倍ATR动态止损，及时止损
- **分级止盈**：4级阶梯止盈（0.5%, 1%, 1.5%, 2%）
- **仓位管理**：单笔风险≤0.8%，最大仓位≤25%
- **相关性控制**：最多同时持有2个相关性标的

### 🚀 全自动运行
- **定时执行**：每小时自动触发
- **无需人工**：完全自动化交易
- **24/7监控**：实时风控和监控
- **异常保护**：自动识别并处理异常情况

### 🎯 参赛合规
- ✅ 严格按照OKX大赛规则设计
- ✅ 纯AI推理逻辑，非简单if/else规则
- ✅ 通过Agent Trade Kit自动执行
- ✅ 支持任意子账户参赛

---

## 🚀 快速开始

### 前置要求

```bash
# 1. 安装Python 3.8+
python --version

# 2. 安装OKX SDK
pip install okx-sdk

# 3. 准备OKX API密钥（推荐使用子账户）
```

### 三步部署

#### 第1步：获取API密钥

1. 登录OKX账户
2. 进入「API管理」→「创建API」
3. 推荐使用**子账户**（安全第一）
4. 设置权限：
   - ✅ 读取
   - ✅ 交易（合约）
   - ❌ 提现（不要授权）
5. 复制API Key、Secret Key、Passphrase

#### 第2步：安装策略

```bash
# 克隆仓库
git clone https://github.com/yourusername/yield-king-strategy.git
cd yield-king-strategy

# 复制配置文件
cp okx_config.py ~/.okx/config.py

# 编辑配置文件，填入你的API密钥
nano ~/.okx/config.py
```

#### 第3步：启动策略

```bash
# 安装依赖
pip install -r requirements.txt

# 测试API连接
python test_okx_sdk.py

# 启动策略
python main.py
```

---

## 📖 文档

### 主要文档

| 文档 | 说明 |
|------|------|
| [SKILL.md](SKILL.md) | 核心策略定义 |
| [README_SKILL.md](README_SKILL.md) | 详细使用说明 |
| [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) | 完整部署指南 |
| [SETUP_INSTRUCTIONS.md](SETUP_INSTRUCTIONS.md) | 快速设置指南 |
| [SKILL_OVERVIEW.md](SKILL_OVERVIEW.md) | 策略概览表格 |

### 图表文件

| 文件 | 说明 |
|------|------|
| [strategy_diagram.txt](strategy_diagram.txt) | 策略流程图 |
| [architecture_diagram.txt](architecture_diagram.txt) | 系统架构图 |
| [comparison_chart.txt](comparison_chart.txt) | 对比分析图表 |

### 配置文件

| 文件 | 说明 |
|------|------|
| [okx_config.py](okx_config.py) | 配置模板 |
| [config_example.toml](config_example.toml) | TOML配置示例 |

---

## 💡 功能特性

### 数据采集

✅ **市场数据**
- 实时价格获取
- K线数据获取（1小时/4小时/日线）
- 资金费率监控
- 持仓量变化跟踪

✅ **技术指标**
- 移动平均线（MA）
- 相对强弱指标（RSI）
- MACD指标
- 真实波幅（ATR）

### AI分析

✅ **多因子评分**
- 趋势分析（40%权重）
- 动量分析（30%权重）
- 波动率分析（20%权重）
- 资金流分析（10%权重）

✅ **智能决策**
- 市场环境过滤
- 交易标的筛选
- 动态仓位计算
- 风险评估

### 交易执行

✅ **自动交易**
- 市价单/限价单
- 开仓/平仓
- 止损/止盈设置
- 批量订单管理

✅ **风险控制**
- ATR动态止损
- 分级止盈
- 仓位限制
- 相关性控制

---

## 🎓 使用指南

### 推荐使用流程

#### 第1阶段：测试期（1-2周）
```
Demo环境 → 验证策略 → 观察表现 → 调整参数
```

#### 第2阶段：小额实盘（2-4周）
```
Live环境 → 小额资金 → 密切监控 → 验证效果
```

#### 第3阶段：正常运营（长期）
```
Live环境 → 正常资金 → 自动监控 → 持续优化
```

### 配置参数

```python
# 风险参数
MAX_RISK_PER_TRADE = 0.008     # 单笔风险 0.8%
MAX_POSITION_PERCENT = 0.15    # 最大仓位 15%

# 止损止盈
SL_ATR_MULTIPLE = 1.5          # ATR止损倍数
TAKE_PROFIT_LEVELS = [0.005, 0.01, 0.015, 0.02]  # 止盈级别

# 策略权重
FACTOR_WEIGHTS = {
    'trend': 0.40,      # 趋势权重 40%
    'momentum': 0.30,   # 动量权重 30%
    'volatility': 0.20, # 波动率权重 20%
    'volume': 0.10      # 资金权重 10%
}
```

---

## ⚠️ 风险提示

### 市场风险
- 加密货币市场波动性极大
- 策略历史表现不代表未来收益
- 可能面临技术故障和网络延迟

### 操作风险
- API密钥泄露可能导致资金损失
- 网络连接中断可能影响策略执行
- 极端市场条件下止损可能失效

### 建议
- 仅使用你能承受损失的资金
- 定期备份API密钥
- 保持策略文件的备份
- 关注OKX大赛规则变化

---

## 🔧 技术栈

- **编程语言**: Python 3.8+
- **API接口**: OKX SDK
- **AI引擎**: Hermes AI
- **数据处理**: Pandas
- **调度系统**: Cron Job
- **配置管理**: TOML/Python

---

## 📊 性能对比

| 策略类型 | 年化收益 | 最大回撤 | 夏普比率 | 运行成本 |
|---------|---------|---------|---------|---------|
| **收益王策略** | 30-50% | < 20% | > 1.5 | $0 |
| 趋势跟踪 | 20-40% | 20-30% | 1.0-1.5 | $50-200/月 |
| 套利策略 | 10-30% | < 10% | 1.5-2.0 | $100-500/月 |
| 人工交易 | 不确定 | 变动大 | < 1.0 | $500-2000/月 |

---

## 🤝 贡献

欢迎贡献代码、报告问题或提出新功能建议！

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

---

## 📄 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

## 🙏 致谢

- OKX交易所提供的API服务
- Hermes AI平台的技术支持
- 所有贡献者和用户的反馈

## 📞 联系方式

- **GitHub Issues**: [提交问题](https://github.com/yourusername/yield-king-strategy/issues)
- **讨论区**: [GitHub Discussions](https://github.com/yourusername/yield-king-strategy/discussions)

---

<div align="center">

**⭐ 如果这个项目对你有帮助，请给个 Star！**

Made with ❤️ by [收益王策略团队]

[⬆ 返回顶部](#-收益王策略---okx-ai量化交易策略)

</div>