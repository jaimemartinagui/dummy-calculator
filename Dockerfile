
FROM python:3.9-slim-bullseye

COPY requirements.txt dummy_calculator/requirements.txt
RUN pip install -r dummy_calculator/requirements.txt

COPY dummy_calculator/main.py /dummy_calculator/main.py
CMD ["python", "dummy_calculator/main.py"]

