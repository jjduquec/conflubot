FROM python:3.12.10  
WORKDIR /usr/local/conflubot_ingestion

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt 

COPY ./*  ./
RUN huggingface-cli download jjduquec/conflubot_embed_model --local-dir ./conflubot_model --local-dir-use-symlinks False 
EXPOSE 8081

CMD ["python", "app.py"] 