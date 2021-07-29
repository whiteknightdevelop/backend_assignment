FROM python:3

WORKDIR /app

COPY api-app/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY api-app/app ./app

CMD [ "python", "app/main.py" ]