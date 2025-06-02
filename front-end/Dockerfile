FROM python:3.12.10  
WORKDIR /usr/local/conflubot_interface

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt 

COPY .streamlit/config.toml  ./.streamlit/config.toml
COPY ./*.py  ./

EXPOSE 8080

CMD ["streamlit", "run","interfaz.py","--server.port","8080"] 