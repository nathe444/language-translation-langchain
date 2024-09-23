import streamlit as st
import os
from deep_translator import GoogleTranslator
from gtts import gTTS
from PyPDF2 import PdfReader
import docx
from io import BytesIO
from langdetect import detect  



# Custom CSS for styling
st.markdown("""
<style>
    .main {
        background-color: #10103c;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 1);
    }
    h1, h2 {
        color: #839ab2;
    }
    .text-input {
        margin-bottom: 20px;
    }
    .subheader {
        color: #785656;
            }
</style>
""", unsafe_allow_html=True)

st.title('🌐 Language Translation App')

# Translation function using deep-translator
def translation(input_text, target_lang):
    try:
        translated_text = GoogleTranslator(target=target_lang).translate(text=input_text)
        return translated_text
    except Exception as e:
        st.error(f"Translation failed: {e}")
        return None

# Language detection using langdetect
def detect_language(input_text):
    try:
        detected_lang = detect(input_text)
        return detected_lang
    except Exception as e:
        st.error(f"Language detection failed: {e}")
        return None

# Extract text from PDF
def extract_text_from_pdf(pdf_file):
    pdf_reader = PdfReader(pdf_file)
    extracted_text = ''
    for page in pdf_reader.pages:
        try:
            extracted_text += page.extract_text()
        except Exception as e:
            st.error(f"Error extracting text from page: {e}")
    return extracted_text

# Extract text from DOCX
def extract_text_from_docx(docx_file):
    doc = docx.Document(docx_file)
    extracted_text = '\n'.join([para.text for para in doc.paragraphs])
    return extracted_text

# Text Input Translation
with st.container():
    st.subheader("Text Input Translation")
    input_text = st.text_area("Enter text to translate:", key="text_input", height=150)

    if input_text:
        detected_lang = detect_language(input_text)
        target_lang = st.selectbox("Select target language:", [
            'english', 'spanish', 'french', 'german', 'italian', 
            'arabic', 'hindi', 'portuguese', 'russian', 'japanese', 
            'korean', 'bengali', 'turkish', 'amharic'
        ])

        if st.button("Translate Text"):
            translated_text = translation(input_text, target_lang)
            st.write(f"Translated text: {translated_text}")

# Document Upload Translation
with st.container():
    st.subheader("Document Upload Translation")
    uploaded_file = st.file_uploader("Upload a document (PDF or Word)", type=['pdf', 'docx'])

    if uploaded_file:
        if uploaded_file.type == 'application/pdf':
            extracted_text = extract_text_from_pdf(uploaded_file)
        elif uploaded_file.type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
            extracted_text = extract_text_from_docx(uploaded_file)

        st.write("Extracted text:", extracted_text[:100] + "...")

        detected_lang = detect_language(extracted_text)

        target_lang_doc = st.selectbox("Select target language for document:", [
            'english', 'spanish', 'french', 'german', 'italian', 
             'arabic', 'hindi', 'portuguese', 
            'russian', 'japanese', 'korean', 'bengali', 'turkish', 'amharic'
        ], key="doc_lang")

        if st.button("Translate Document upto 10000 characters"):
            translated_doc_text = translation(extracted_text, target_lang_doc)
            if translated_doc_text:
                st.write(f"Translated document text: {translated_doc_text[:10000]}...") 

