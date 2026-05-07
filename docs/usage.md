# 使用说明

## 🎯 快速开始

### 安装依赖
```bash
pip install -r requirements.txt
```

### 基本使用
```python
from scripts.doc_formatter import DocFormatter

# 创建格式化器实例
formatter = DocFormatter()

# 格式化文档
formatter.format_document("input.docx", "output.md")
```

### 命令行使用
```bash
# 安装后使用
python -m scripts.doc_formatter --input input.docx --output output.md

# 或者使用安装后的命令
doc-formatter --input input.docx --output output.md
```

## 📖 详细教程

### 1. 作为独立工具使用
```python
from scripts.doc_formatter import DocFormatter

formatter = DocFormatter(
    font_name="微软雅黑",  # 字体
    font_size=12,          # 字号
    output_format="both"   # 输出格式：both/md/docx
)

# 处理单个文件
formatter.process_file("作业文档.docx")

# 批量处理
formatter.batch_process("作业文件夹/")
```

### 2. 在OpenClaw中使用
1. 将整个 `doc-formatter` 目录复制到 `workspace/skills/`
2. 重启OpenClaw
3. 使用命令：
   ```
   请帮我格式化 memory/我的作业.docx
   ```

### 3. 自定义配置
创建 `config.json`：
```json
{
  "font_name": "宋体",
  "font_size": 12,
  "output_format": "both",
  "auto_numbering": true,
  "fix_titles": true,
  "fix_lists": true
}
```

然后使用：
```python
formatter = DocFormatter(config_file="config.json")
```

## 🔧 高级功能

### 自定义格式化规则
```python
from scripts.doc_formatter import DocFormatter

# 自定义规则
custom_rules = {
    "title_patterns": [
        r"^第[一二三四五六七八九十]+章",  # 识别章节标题
        r"^\d+\.\s+",                     # 识别数字标题
    ],
    "list_patterns": [
        r"^[•○●▪▫]",                     # 无序列表
        r"^\d+[\.\)]",                    # 有序列表
    ]
}

formatter = DocFormatter(custom_rules=custom_rules)
```

### 批量处理
```python
# 处理整个目录
formatter.batch_process(
    input_dir="input_folder/",
    output_dir="output_folder/",
    file_pattern="*.docx"
)

# 生成处理报告
report = formatter.generate_report()
print(report)
```

## 🎨 输出格式

### Markdown输出
- 保留所有文本内容
- 转换标题为Markdown语法
- 转换列表为Markdown语法
- 保留加粗和斜体

### Word输出
- 使用规范的中文字体
- 统一标题样式
- 规范列表格式
- 优化段落间距

## 📊 示例

### 输入文档（混乱格式）
```
第一章 绪论
  1.1研究背景
• 项目重要性
  • 社会需求
```

### 输出文档（规范格式）
```markdown
# 第一章 绪论

## 1.1 研究背景

- 项目重要性
  - 社会需求
```

## ⚠️ 注意事项

1. **字体支持**：确保系统安装了相应中文字体
2. **文件编码**：建议使用UTF-8编码
3. **复杂格式**：表格、图片等复杂格式可能需要手动调整
4. **文件大小**：建议文档不超过10MB

## 🔍 故障排除

### 常见问题
1. **中文乱码**：检查系统字体和文件编码
2. **格式丢失**：尝试简化复杂格式
3. **内存不足**：分批次处理大文档

### 调试模式
```python
formatter = DocFormatter(debug=True)
formatter.process_file("input.docx")
```

## 📞 支持

如有问题，请：
1. 查看 [FAQ](docs/faq.md)
2. 提交 [Issue](https://github.com/yourusername/doc-formatter/issues)
3. 查看示例代码