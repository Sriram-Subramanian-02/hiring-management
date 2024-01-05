from flask import Blueprint, request, jsonify
from PyPDF2 import PdfReader

resume_shortlisting = Blueprint('resume_shortlisting', __name__)

def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, 'rb') as file:
        pdf_reader = PdfReader(file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text

@resume_shortlisting.route('/resume_upload', methods=['POST'])
def upload_file():
    print("hi")
    print(request)
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file and file.filename.endswith('.pdf'):
        try:
            file_path = 'F://hiring-management//uploads//' + file.filename
            file.save(file_path)
            text = extract_text_from_pdf(file_path)
            return jsonify({'text': text})
        except Exception as e:
            return jsonify({'error': str(e)})

    return jsonify({'error': 'Invalid file format. Please upload a PDF file'})
