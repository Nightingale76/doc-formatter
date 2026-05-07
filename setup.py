from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="doc-formatter",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="大学生作业文档格式转换工具",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/doc-formatter",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Text Processing",
        "Topic :: Education",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "doc-formatter=scripts.doc_formatter:main",
        ],
    },
)