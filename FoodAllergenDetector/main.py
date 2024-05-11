from flask import *
import pytesseract
from PIL import Image
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/extract_text', methods=['POST'])
def extract_text():
    if 'image' not in request.files:
        return "No image uploaded"

    image = request.files['image']
    img_bytes = image.read()
    img = Image.open(io.BytesIO(img_bytes))

    # Use pytesseract to extract text from the image
    text = pytesseract.image_to_string(img)

    return render_template('result.html', text=text)

if __name__ == '__main__':
    app.run(debug=True)
