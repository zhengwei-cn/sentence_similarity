# 使用官方的 Python 基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制当前目录内容到工作目录中
COPY . /app

# 安装必要的依赖
RUN pip install --no-cache-dir -r requirements.txt


# 设置环境变量以避免生成 pyc 文件
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 复制默认配置文件到镜像中
COPY config.toml /app/config.toml

# 启动应用
CMD ["python", "app.py"]
