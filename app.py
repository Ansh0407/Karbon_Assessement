from flask import Flask, render_template, request, redirect, url_for, flash
import json
from model import probe_model_5l_profit

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)

    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    if file:
        data = json.load(file)
        result = probe_model_5l_profit(data["data"]) 
        return render_template('result.html', result=result) 

if __name__ == '__main__':
    app.run(debug=True)
