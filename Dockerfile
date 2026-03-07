FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install pandas

CMD ["sh", "-c", "python duplicate_cells.py && python add.py"]
