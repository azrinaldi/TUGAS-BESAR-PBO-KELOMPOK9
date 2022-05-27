FROM python:3.9.9

ADD main.py .

RUN pip install pygame

CMD [ "python", "./main.py" ]