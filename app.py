from flask import Flask, render_template, request, redirect, url_for, flash
import json
from model import probe_model_5l_profit
import os
from dotenv import load_dotenv  # Import to load environment variables

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Set secret key using environment variable or fallback
app.secret_key = os.getenv('SECRET_KEY', 'fallbacksecret')

@app.route('/')
def index():
    """Render the home page (index.html)."""
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file upload, process data, and render result page."""
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)

    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    if file:
        try:
            data = json.load(file)  # Load JSON data from uploaded file
            result = probe_model_5l_profit(data["data"])  # Process data using the model
            return render_template('result.html', result=result)
        except json.JSONDecodeError:
            flash('Invalid JSON file format')
            return redirect(request.url)
        except KeyError:
            flash('Invalid JSON data. Expected key: "data"')
            return redirect(request.url)

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)), debug=True)
