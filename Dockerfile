FROM python:3.9

# 设置 python 环境变量
ENV PYTHONUNBUFFERED 1

# 创建 code 文件夹并将其设置为工作目录
RUN mkdir /code
WORKDIR /code

# 更新 pip
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pip -U
# 设置清华源
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

# 安装库
RUN pip install pytest numpy pandas matplotlib

# 将当前目录复制到容器的 code 目录
ADD . /code/
# 使用交互式启动命令，如启动一个 Shell，保持容器交互性
CMD ["python3"]