from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from ChatBoxSystem.RAG.RAG import RAG


app = Flask(__name__)
CORS(app)

chat_system = RAG()

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    query = data.get('query', '')
    if not query:
        return jsonify({'error': 'Query is required'}), 400

    try:
        answer = chat_system.answer_query(query)
        return jsonify({'answer': answer})
    except Exception as e:
        return jsonify({'error': 'Internal server error'}), 500
    
@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
