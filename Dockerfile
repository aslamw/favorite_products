FROM python:3.11.3-alpine3.18

#WORKDIR /usr/src/app

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .


#EXPOSE 6060

CMD [ "python","./app.py" ]