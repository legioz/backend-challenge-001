FROM python:3.9

LABEL version="1.0.0"
LABEL autor="luizfelipevbll@gmail.com"

ENV DOCKER_ON=True
ENV DEBUG=True
ENV TZ="America/Sao_Paulo"

RUN date
RUN apt-get update && apt-get install -y apt-utils
RUN apt-get install -y \
    curl \
    vim \
    default-libmysqlclient-dev \
    build-essential \
    python3-pip \
    bash-completion \
    libmariadb-dev \
    && apt-get autoremove -y \
    && apt-get autoclean -y


RUN mkdir -p /src
COPY ./ /src
WORKDIR /src

RUN python -m pip install --upgrade pip
RUN pip install wheel setuptools
RUN pip install -r requirements.txt 

EXPOSE 8000

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
