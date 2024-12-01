import os
from flask import Flask, render_template, request, redirect, session, url_for
import openai

app = Flask(__name__)
app.secret_key = 'sfox1234'

# Load OpenAI API key from environment variables
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        session['name'] = request.form['name']
        return redirect(url_for('upload'))
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        description = request.form['description']
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": description}
            ]
        )
        message = response['choices'][0]['message']['content']
        return render_template('success.html', message=message)
    name = session.get('name', 'Guest')
    return render_template('upload.html', name=name)

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
