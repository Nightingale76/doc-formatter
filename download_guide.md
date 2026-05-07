# 下载指南

由于OpenClaw界面可能只支持下载单个文件，这里提供几种下载整个项目的方法：

## 方法一：使用Git（推荐）

### 在终端中：
```bash
# 克隆整个项目
git clone https://github.com/yourusername/doc-formatter.git

# 进入项目目录
cd doc-formatter

# 安装依赖
pip install -r requirements.txt
```

### 在OpenClaw中：
```bash
# 使用exec命令
exec git clone https://github.com/yourusername/doc-formatter.git
```

## 方法二：手动下载所有文件

如果只能下载单个文件，请按以下顺序下载：

### 必需文件（按优先级）：
1. **核心文件**：
   - `scripts/doc_formatter.py` - 主程序
   - `requirements.txt` - 依赖列表
   - `README.md` - 使用说明

2. **配置文件**：
   - `setup.py` - 安装脚本
   - `.gitignore` - Git忽略文件
   - `LICENSE` - 许可证

3. **文档和示例**：
   - `docs/usage.md` - 详细使用说明
   - `examples/` 目录下的所有文件
   - `SKILL.md` - OpenClaw技能定义

### 创建目录结构：
```
doc-formatter/
├── scripts/
│   └── doc_formatter.py
├── examples/
│   ├── usage_example.md
│   ├── 作业提交_test_document.docx
│   └── 格式化后的_test_document.md
├── docs/
│   └── usage.md
├── tests/
│   └── test_formatter.py
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── setup.py
└── SKILL.md
```

## 方法三：使用curl或wget批量下载

### 下载脚本示例：
```bash
#!/bin/bash
# 创建目录
mkdir -p doc-formatter/{scripts,examples,docs,tests}

# 下载核心文件
curl -L -o doc-formatter/scripts/doc_formatter.py \
  https://raw.githubusercontent.com/yourusername/doc-formatter/main/scripts/doc_formatter.py

curl -L -o doc-formatter/requirements.txt \
  https://raw.githubusercontent.com/yourusername/doc-formatter/main/requirements.txt

curl -L -o doc-formatter/README.md \
  https://raw.githubusercontent.com/yourusername/doc-formatter/main/README.md

# 下载其他文件（根据需要添加）
```

## 方法四：使用GitHub API

```python
import requests
import os

def download_file(url, local_path):
    response = requests.get(url)
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    with open(local_path, 'wb') as f:
        f.write(response.content)

# 文件列表
files = [
    ("scripts/doc_formatter.py", "doc-formatter/scripts/doc_formatter.py"),
    ("requirements.txt", "doc-formatter/requirements.txt"),
    ("README.md", "doc-formatter/README.md"),
    # 添加更多文件...
]

base_url = "https://raw.githubusercontent.com/yourusername/doc-formatter/main/"

for remote_path, local_path in files:
    url = base_url + remote_path
    download_file(url, local_path)
    print(f"Downloaded: {local_path}")
```

## 方法五：在OpenClaw中直接使用

如果你只需要在OpenClaw中使用，最简单的方法是：

1. **只下载核心文件**：
   - `SKILL.md`
   - `scripts/doc_formatter.py`
   - `requirements.txt`

2. **手动创建目录**：
   ```bash
   mkdir -p /workspace/projects/workspace/skills/doc-formatter/{scripts,examples}
   ```

3. **复制文件**：
   ```bash
   cp SKILL.md /workspace/projects/workspace/skills/doc-formatter/
   cp scripts/doc_formatter.py /workspace/projects/workspace/skills/doc-formatter/scripts/
   ```

## 📦 最小化安装

如果只需要基本功能，只需要以下文件：
1. `scripts/doc_formatter.py`
2. `requirements.txt`
3. `SKILL.md`（如果是OpenClaw环境）

## 🔧 验证安装

安装完成后，运行测试：
```bash
cd doc-formatter
python scripts/doc_formatter.py --help
```

或者运行测试：
```bash
python tests/test_formatter.py
```

## ❓ 常见问题

### Q: 下载后文件不全怎么办？
A: 检查是否下载了所有必需文件，参考上面的"必需文件"列表。

### Q: 如何知道文件下载成功？
A: 检查文件大小，核心文件 `doc_formatter.py` 应该有几KB大小。

### Q: 下载速度慢怎么办？
A: 可以尝试使用GitHub的镜像站点，或者只下载必需文件。

### Q: 在OpenClaw中如何批量下载？
A: 可以使用循环命令：
```bash
for file in file1 file2 file3; do
  curl -O https://raw.githubusercontent.com/yourusername/doc-formatter/main/$file
done
```

## 📞 支持

如果下载遇到问题，请：
1. 检查网络连接
2. 确认GitHub仓库地址正确
3. 尝试使用不同的下载方法
4. 在GitHub Issues中提问