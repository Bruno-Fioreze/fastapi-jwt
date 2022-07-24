FROM python:3.8-alpine

#set workdir

WORKDIR /app

#Copy project
COPY . .

RUN echo $(ls -1 /)
RUN echo $(ls -1 /fastapi-jwt)

#set enviroment
ENV PYTHONPATH=${PYTHONPATH}:${PWD} 
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

#install dependencies
RUN apk add --update --virtual .tmp-build-deps \
    gcc libc-dev linux-headers  \
    && apk add libffi-dev

#configure poetry
RUN pip install --upgrade pip
RUN pip3 install poetry

RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

ENTRYPOINT ["./entrypoint.sh"]