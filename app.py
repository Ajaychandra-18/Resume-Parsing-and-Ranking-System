
from flask import Flask, render_template, request
import PyPDF2
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Extract text from PDF
def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfFileReader(file)
    text = ''
    for page_num in range(pdf_reader.numPages):
        text += pdf_reader.getPage(page_num).extractText()
    return text

# Placeholder for your ranking logic
def calculate_percentage(similarity_score):
    # Replace this with your actual percentage calculation logic
    return similarity_score * 100

# Your resume parsing and ranking logic goes here

@app.route('/')
def index():
    # Render the main page
    return render_template('index.html')

@app.route('/parse', methods=['POST'])
def parse_resume():
    # Get the uploaded resume file
    uploaded_file = request.files['resume']
    resume_content = extract_text_from_pdf(uploaded_file)

    # Perform resume parsing and ranking
    # ...

    # Placeholder for similarity score (replace this with your actual score)
    similarity_score = 0.85

    # Calculate the percentage (you need to adapt this based on your ranking)
    percentage = calculate_percentage(similarity_score)

    # Placeholder for rank (replace this with your actual rank)
    rank = 1

    # Render the result page with the rank and percentage
    return render_template('result.html', rank=rank, percentage=percentage)

if __name__ == '__main__':
    app.run(debug=True)

