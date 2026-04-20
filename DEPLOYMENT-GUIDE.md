# GitHub 部署指南

本文档详细说明如何将本项目部署到 GitHub 并启用 GitHub Pages。

## 前置要求

1. **安装 Git**
   - 下载地址：https://git-scm.com/download/win
   - 安装后重启 VSCode 或命令行工具
   - 验证安装：`git --version`

2. **注册 GitHub 账号**
   - 访问 https://github.com 注册免费账号

## 部署步骤

### 方法一：使用命令行（推荐）

#### 1. 初始化 Git 仓库

在项目根目录打开终端，执行：

```bash
# 初始化 Git 仓库
git init

# 添加所有文件到暂存区
git add .

# 提交更改
git commit -m "Initial commit: Ancient Architecture Visualization project"
```

#### 2. 创建 GitHub 仓库

1. 访问 https://github.com/new
2. 填写仓库信息：
   - **Repository name**: `ancient-architecture-visualization`（或其他你喜欢的名称）
   - **Description**: `中国古代建筑可视化对比展示 - 抬梁式与穿斗式结构分析`
   - **Public/Private**: 选择 Public（公开）
   - **不要勾选** "Initialize this repository with a README"
3. 点击 "Create repository"

#### 3. 关联远程仓库并推送

创建仓库后，GitHub 会显示类似以下的命令：

```bash
# 添加远程仓库（将 YOUR_USERNAME 替换为你的 GitHub 用户名）
git remote add origin https://github.com/YOUR_USERNAME/ancient-architecture-visualization.git

# 推送到 GitHub
git branch -M main
git push -u origin main
```

### 方法二：使用 VSCode Git 集成

1. **初始化仓库**
   - 点击左侧活动栏的 "源代码管理" 图标（或按 `Ctrl+Shift+G`）
   - 点击 "Initialize Repository" 按钮

2. **提交更改**
   - 在消息框中输入提交信息，如 "Initial commit"
   - 点击 ✓ 按钮提交

3. **发布到 GitHub**
   - 点击左下角的 "Publish Branch" 按钮
   - 选择 "Publish to GitHub private repository" 或 "Publish to GitHub public repository"
   - 按照提示完成操作

## 启用 GitHub Pages

### 步骤 1：配置 GitHub Pages

1. 进入你的 GitHub 仓库页面
2. 点击顶部的 "Settings" 标签
3. 在左侧菜单中找到 "Pages"
4. 在 "Build and deployment" 部分：
   - **Source**: 选择 "Deploy from a branch"
   - **Branch**: 选择 "main" 和 "/ (root)"
   - 点击 "Save"

### 步骤 2：等待部署

- GitHub 会自动部署你的网站
- 通常需要 1-5 分钟
- 刷新页面后，你会看到类似这样的 URL：
  ```
  https://YOUR_USERNAME.github.io/ancient-architecture-visualization/
  ```

### 步骤 3：访问你的网站

直接在浏览器中访问上述 URL 即可查看你的在线网站！

## 更新网站

当你修改代码后，推送更新：

```bash
# 查看更改的文件
git status

# 添加更改的文件
git add .

# 提交更改
git commit -m "描述你的更改"

# 推送到 GitHub
git push
```

GitHub Pages 会自动重新部署，通常几分钟内生效。

## 常见问题

### 1. 图表不显示？
- 检查浏览器控制台是否有错误
- 确保 ECharts CDN 可以正常访问
- 如果离线使用，需要下载 ECharts 到本地

### 2. 路径问题？
- GitHub Pages 使用子路径，确保所有资源使用相对路径
- 本项目已正确使用相对路径，无需修改

### 3. 自定义域名？
- 在 Settings > Pages 中可以配置自定义域名
- 需要在 DNS 提供商处配置 CNAME 记录

## 项目结构说明

```
ancient-architecture-visualization/
├── index.html              # 主页面
├── dashboard.html          # 仪表盘页面
├── css/                    # 样式文件
├── js/                     # JavaScript 文件
├── data/                   # 数据文件
├── assets/                 # 图片资源
├── models/                 # 3D 模型
└── docs/                   # 文档
```

## 技术栈

- **前端**: HTML5 + CSS3 + JavaScript (ES6+)
- **可视化**: ECharts 5.4.3
- **3D 支持**: Three.js
- **部署**: GitHub Pages（静态托管）

## 相关链接

- [GitHub Pages 官方文档](https://docs.github.com/en/pages)
- [ECharts 官方文档](https://echarts.apache.org/)
- [项目 README](./README.md)

---

**祝你部署顺利！** 🎉
