
from flask import Flask, request, jsonify 
from flask_cors import CORS #for handling cross-origin requests
from PyPDF2 import PdfReader #for reading texts from pdfs
import io 


import openai

# Set the OpenAI API key
openai_api_key = "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"

headers = {'Authorization': 'Bearer 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'} #authentication for openAI key

app = Flask(__name__)
CORS(app) #allows browser to permit requests from specified origins.

@app.route('/', methods=['POST', 'GET'])
def upload():
    if request.method == 'GET':
        return '''
        <html>
            <body>
				<div style='border: bold;'>
					<form action="/" method="post" enctype="multipart/form-data">
						Select a .pdf or .txt file to upload:
						<input type="file" name="file"><br><br>
						<input type="submit" value="Upload">
					</form>
                </div>
            </body>
        </html>
        '''

    file = request.files.get('file') # What user uploads

    if not file:
        return jsonify({'error': 'No file provided'}), 400

    try:
        if file.filename.endswith('.pdf'):
            reader = PdfReader(file)

            if reader.is_encrypted:
                return jsonify({'error': 'Encrypted PDFs are not supported'}), 400

            text = '' #This is the data
            for page_num in range(len(reader.pages)):
                text += reader.pages[page_num].extract_text()

            if not text.strip():
                return jsonify({'error': 'No text found in the PDF'}), 400

        elif file.filename.endswith('.txt'):
            try:
                text = file.read().decode('utf-8') #This is the data
            except UnicodeDecodeError:
                return jsonify({'error': 'Unable to decode text file. Ensure it is UTF-8 encoded.'}), 400

        else:
            return jsonify({'error': 'Unsupported file type'}), 400

        return jsonify({'text': text})

    except Exception as e:
        return jsonify({'error': str(e)}), 500



if __name__ == '__main__':
    app.run(debug=True)
