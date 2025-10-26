FROM python:3.11.5

RUN mkdir /prepare_mgtu

WORKDIR /prepare_mgtu

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
