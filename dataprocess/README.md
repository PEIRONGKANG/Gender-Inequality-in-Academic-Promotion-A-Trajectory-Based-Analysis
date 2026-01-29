# JP Researcher Scientific Reports

日本学者科研数据处理项目 - 用于处理和分析日本学者的JSON元数据

## 项目简介

本项目用于处理从 researchmap 官方 API 获取的日本学者 JSON 元数据，提取关键信息并保存为 CSV 格式，便于后续数据分析。

## 目录结构

```
jpresearcher_scientific_reports/
├── src/
│   ├── env.toml              # 环境配置文件（需要手动创建）
│   └── resolver/             # 数据处理脚本
│       ├── researchers_resolve.py              # 提取研究者基本信息
│       ├── researcher_education_resolve.py     # 提取教育经历
│       ├── researcher_degree_resolve.py        # 提取学位信息
│       └── researchers_experience_resolve.py   # 提取研究经历
├── static/
│   ├── sample/               # JSON 元数据文件（10,000条示例数据）
│   ├── sampleresolver/       # CSV 输出目录（自动生成）
│   └── prompt/               # 提示词模板
│       └── extract_job_title.txt
├── pyproject.toml            # 项目配置和依赖
├── uv.lock                   # 依赖锁定文件
└── README.md                 # 本文件
```

## 快速开始

### 1. 环境要求

- Python 3.11+
- uv 包管理器

### 2. 安装 uv（如果尚未安装）

**Windows (PowerShell):**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**macOS/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 3. 克隆项目

```bash
git clone https://github.com/995414558/jpresearcherscientificreports.git
cd jpresearcherscientificreports
```

### 4. 创建环境配置文件 ⚠️ **重要**

在运行项目之前，**必须**先创建 `src/env.toml` 文件：

```bash
# 创建文件
touch src/env.toml  # Linux/macOS
# 或
New-Item -Path "src/env.toml" -ItemType File  # Windows PowerShell
```

然后编辑 `src/env.toml`，添加以下内容：

```toml
base_url = "https://api.chatanywhere.tech/v1"
api_key = "your-api-key-here"
```

> **注意**：
> - 请将 `your-api-key-here` 替换为您的实际 API 密钥
> - 此文件包含敏感信息，已被添加到 `.gitignore`，不会被提交到 Git

### 5. 安装依赖

```bash
uv sync
```

### 6. 运行数据处理脚本

```bash
# 提取研究者基本信息
uv run python src/resolver/researchers_resolve.py

# 提取教育经历
uv run python src/resolver/researcher_education_resolve.py

# 提取学位信息
uv run python src/resolver/researcher_degree_resolve.py

# 提取研究经历
uv run python src/resolver/researchers_experience_resolve.py
```

### 7. 查看输出结果

处理完成后，CSV 文件将保存在 `static/sampleresolver/` 目录下：

- `jp_researchers.csv` - 研究者基本信息
- `jp_researchers_education.csv` - 教育经历
- `jp_researchers_degrees.csv` - 学位信息
- `jp_researchers_research_experience.csv` - 研究经历

## 数据说明

### 输入数据
- **位置**: `static/sample/`
- **格式**: JSON
- **数量**: 10,000 条示例数据
- **来源**: researchmap 官方 API

### 输出数据
- **位置**: `static/sampleresolver/`
- **格式**: CSV (UTF-8 编码)
- **说明**: 提取的结构化数据，便于后续分析



## 注意事项

1. ⚠️ **必须先创建 `src/env.toml` 文件**才能运行项目
2. 📁 `static/sampleresolver/` 目录会在首次运行时自动创建
3. 🔒 `env.toml` 文件包含 API 密钥，请勿分享或提交到 Git
4. 📊 处理 10,000 条数据大约需要几分钟时间


