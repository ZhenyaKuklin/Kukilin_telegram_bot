FROM python:3.10-slim
ENV  TOKEN = 'Your token'
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "bot.py"]