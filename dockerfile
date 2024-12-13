FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && \
    pip install -r requirements.txt
COPY . /app
EXPOSE 8080
CMD ["python", "gateway.py"]