from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session management

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Store the name in the session
        session['name'] = request.form['name']
        return redirect('/upload')
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Handle the file the user uploads
        file = request.files['file']
        if file and file.filename.endswith('.png'):
            # Assuming the file is valid and saving it is handled here
            # Generate a motivational message
            message = "Keep pushing forward, you're doing great!"
            return render_template('success.html', message=message)
    # If GET or no file has been uploaded
    name = session.get('name', 'Guest')
    return render_template('upload.html', name=name)

@app.route('/success')
def success():
    # Display the motivational message
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
