# 🚀 GitHub上传指南

## 方式1：使用GitHub CLI（推荐）

### 第1步：登录GitHub
```bash
cd ~/yield-king-strategy
gh auth login
```
按照提示操作：
1. 选择 GitHub.com
2. 选择 HTTPS 或 SSH
3. 浏览器授权登录

### 第2步：创建仓库
```bash
cd ~/yield-king-strategy
gh repo create yield-king-strategy --public --source=. --push
```

### 完成！
仓库已创建并推送到GitHub，链接为：
`https://github.com/你的用户名/yield-king-strategy`

---

## 方式2：手动上传

### 第1步：在GitHub创建仓库
1. 访问 https://github.com/new
2. 仓库名称：`yield-king-strategy`
3. 可见性：公开（Public）
4. 点击"Create repository"

### 第2步：推送到GitHub
```bash
cd ~/yield-king-strategy
git branch -M main
git remote add origin https://github.com/你的用户名/yield-king-strategy.git
git push -u origin main
```

### 完成！
仓库已上传到GitHub。

---

## 📦 当前仓库内容

```
yield-king-strategy/
├── README.md                 # 主文档（已创建）
├── SKILL.md                 # 核心策略定义（已创建）
├── main.py                  # 主运行脚本（已创建）
├── requirements.txt         # 依赖包列表（已创建）
├── LICENSE                  # MIT许可证（已创建）
└── GITHUB_SETUP.md          # 本文件
```

---

## 🎯 下一步

### 完整功能版本
如需包含完整文档和图表，添加以下文件：

```bash
# 复制完整文档（如果有源文件）
cp /path/to/source/files/*.md .
cp /path/to/source/files/*.txt .
cp /path/to/source/files/*.py .

# 提交并推送
git add .
git commit -m "Add complete documentation"
git push origin main
```

---

## 💡 快速检查清单

上传前确认：
- [ ] README.md 已完善
- [ ] SKILL.md 已包含完整策略
- [ ] LICENSE 已添加
- [ ] requirements.txt 已更新
- [ ] 没有敏感信息（API密钥等）
- [ ] 文件结构合理

---

## 🔧 常见问题

### Q: 推送失败怎么办？
A: 检查是否有权限，确认远程URL是否正确。

### Q: 如何更新仓库？
A: 
```bash
git add .
git commit -m "Update description"
git push origin main
```

### Q: 如何删除仓库？
A: 在GitHub网站进入仓库 → Settings → Danger Zone → Delete repository

---

## 🎉 准备好了吗？

选择上面的方式上传到GitHub，完成后就能获得：
- 完整的项目页面
- Star和Fork功能
- Issue和Pull Request支持
- 自动化的CI/CD

**立即开始上传！** 🚀