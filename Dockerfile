# Base Image
FROM python:3.8

# created and set working directory
RUN mkdir /app
WORKDIR /app

# Add current working directory to working directory.
ADD . /app/
# COPY . /app/

# set default enviroment varible
ENV PYTHONUNBUFFER 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninterative

# set project enviroment varibles
ENV PORT=8000

# Install depenencies
RUN apt-get update && apt-get install -y --no-install-recommends \
        tzdata \
        python3-setuptools \
        python3-dev \
        python3-venv \
        git \
        && \
        apt-get clean && \
        rm -rf /var/lib/apt/lists/*

# install enviroment depenencies
RUN pip3 install --upgrade pip
RUN pip3 install pipenv

# install project depenencies
RUN pipenv install

EXPOSE 8888
# CMD cd NOTE_MANAGER/
# CMD pipenv run gunicorn NOTE_MANAGER.wsgi:application --bind 0.0.0.0:$PORT
CMD ["bash","-c","cd ./NOTE_MANAGER/ && pipenv run gunicorn NOTE_MANAGER.wsgi --bind 0.0.0.0:$PORT --log-file -"]

