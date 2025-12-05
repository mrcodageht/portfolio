FROM python:3.13

WORKDIR /code

COPY /auth/requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY /auth/app/ /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8070"]

