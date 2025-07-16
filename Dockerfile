#Dockerfile

# 🐳 Container-ready app config
FROM python:3.11-slim

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app/smolagent_studio.py"]

🚀 Build with docker build -t smolagent-studio . Run with docker run -p 7860:7860 smolagent-studio