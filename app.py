from flask import Flask, request, jsonify, render_template
import openai

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    # File upload logic here...
    return jsonify({'response': 'File processed'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
