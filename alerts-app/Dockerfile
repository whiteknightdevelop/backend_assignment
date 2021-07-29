FROM python:3

WORKDIR /app

COPY alerts-app/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY alerts-app/app ./app
RUN mkdir /config
COPY ../../config.yml ./app
VOLUME /config
CMD [ "python", "app/main.py" ]