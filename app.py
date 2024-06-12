from flask import Flask, render_template, request, make_response, session
from werkzeug.utils import secure_filename
import os
from PIL import Image
import numpy as np
import csv

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'static/uploads/'
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return 'No file uploaded', 400

    file = request.files['image']

    if file.filename == '':
        return 'No file selected', 400

    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    hex_colors = analyze_colors(file_path)
    
    return render_template('index.html', uploaded_image=filename, hex_colors=hex_colors)
    


def analyze_colors(image_path):
    image = Image.open(image_path)
    image = image.convert('RGB')
    image_data = np.array(image)
    pixels = image_data.reshape(-1, 3)
    color_counts = {}
    for pixel in pixels:
        color = tuple(pixel)
        color_counts[color] = color_counts.get(color, 0) + 1
    
    sorted_colors = sorted(color_counts.items(), key=lambda x: x[1], reverse=True)

    top_colors = sorted_colors[:10]

    # Convert RGB values to hex codes
    hex_colors = []
    for color, count in top_colors:
        hex_color = '#%02x%02x%02x' % color
        hex_colors.append((hex_color, count))

    return hex_colors

if __name__ == '__main__':
    app.run(debug=True)