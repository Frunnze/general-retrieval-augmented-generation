FROM python:3.12-slim

WORKDIR /app
COPY . ./

RUN pip install -r requirements.txt

CMD ["uvicorn", "run:app", "--host", "0.0.0.0", "--port", "8000"]