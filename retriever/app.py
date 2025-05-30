from flask import Flask ,jsonify ,request 
from retriever import ask_question

app= Flask(__name__)

@app.route('/api/ask_question/',methods=['GET'])
def get_link():
    json=request.get_json(force=True)
    question=json.get('question')
    message=ask_question(question)
    return jsonify({'message':message})


if __name__=='__main__':
    app.run(host='0.0.0.0',port=8082)