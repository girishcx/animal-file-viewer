from flask import Flask, request, jsonify, send_from_directory, render_template
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
IMAGE_FOLDER = 'static/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get-image')
def get_image():
    animal = request.args.get('animal')
    image_map = {
        'cat': 'cat.jpg',
        'dog': 'dog.jpg',
        'elephant': 'elephant.jpg'
    }
    filename = image_map.get(animal)
    return jsonify({'image_url': f'/static/images/{filename}'})

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)
    return jsonify({
        'name': file.filename,
        'size': os.path.getsize(filepath),
        'type': file.content_type
    })

@app.route('/static/images/<filename>')
def serve_image(filename):
    return send_from_directory(IMAGE_FOLDER, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
