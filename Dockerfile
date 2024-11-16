FROM python:3.9

RUN mkdir /Recruit

WORKDIR /Recruit

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .