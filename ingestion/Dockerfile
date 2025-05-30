FROM python:3.12.10  
WORKDIR /usr/local/conflubot_ingestion

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt 

COPY ./*  ./
COPY ./conflubot_model  ./conflubot_model/
EXPOSE 8081 

CMD ["python", "app.py"] 