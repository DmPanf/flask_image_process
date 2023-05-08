from flask import Flask, render_template, request, send_file
import os
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_image', methods=['POST'])
def process_image():
    # Здесь должен быть ваш код для обработки изображений
    # Сохраните обработанное изображение в виде файла
    # (для демонстрации используется просто загруженное изображение)
    image = request.files['image']
    return send_file(io.BytesIO(image.read()), attachment_filename='segmented.png', mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
