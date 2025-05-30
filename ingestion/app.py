from flask import Flask ,jsonify ,request 
from ingestion import get_repository

app= Flask(__name__)

@app.route('/api/get_repository/',methods=['GET'])
def get_link():
    json=request.get_json(force=True)
    url=json.get('url')
    message=get_repository(url)
    return jsonify({'message':message})


if __name__=='__main__':
    app.run(host='0.0.0.0',port=8081)