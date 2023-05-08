FROM python:3.9-bullseye

WORKDIR /app

COPY . .

ENV SECRET='5547e593f05c31ce94aaf75ee7d9a0036798c3475154f12c8faa08dc9659d7fd'

RUN pip install -r requirements.txt

CMD ["python", "main.py"]