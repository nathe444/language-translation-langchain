import streamlit as st
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
        h1 {
            color: #839ab2;
        }
        .custom-subheader {
            color: #34dde0;
            font-size: 26px;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .text-input {
            margin-bottom: 20px;
        }
        .stTextArea textarea, .stTextInput input {
            background-color: #333;
            color: #f1f1f1;
            border-radius: 8px;
            border: 1px solid #666;
        }
        .stButton > button {
            background-color: #4CAF50;
            color: white;
            border-radius: 8px;
            padding: 10px 20px;
            border: none;
        }
        .stButton > button:hover {
            background-color: #45a049;
        }
            
        .custom-subheader:nth-child(1) {
                margin-top: 40px;
            }

        @media (max-width: 768px) {
            h1 {
                font-size: 22px;
            }
            .custom-subheader {
                font-size: 20px;
            }
        }
        @media (max-width: 480px) {
            h1 {
                font-size: 20px;
            }
            .custom-subheader {
                font-size: 18px; 
            }
            
        }
    </style>
""", unsafe_allow_html=True)

st.title('🌐 Language Translation App')

# Text Input Translation with Custom Subheader
st.markdown('<div class="custom-subheader">Text Input Translation</div>', unsafe_allow_html=True)
input_text = st.text_area("Enter text to translate:", key="text_input", height=150)

if input_text:
    detected_lang = detect(input_text)
    target_lang = st.selectbox("Select target language:", [
        'english', 'spanish', 'french', 'german', 'italian', 
        'arabic', 'hindi', 'portuguese', 'russian', 'japanese', 
        'korean', 'bengali', 'turkish', 'amharic'
    ])

    if st.button("Translate Text"):
        translated_text = GoogleTranslator(target=target_lang).translate(text=input_text)
        st.write(f"Translated text: {translated_text}")

# Document Upload Translation
st.markdown('<div class="custom-subheader">Document Upload Translation</div>', unsafe_allow_html=True)
uploaded_file = st.file_uploader("Upload a document (PDF or Word)", type=['pdf', 'docx'])

if uploaded_file:
    if uploaded_file.type == 'application/pdf':
        pdf_reader = PdfReader(uploaded_file)
        extracted_text = ''.join([page.extract_text() for page in pdf_reader.pages])
    elif uploaded_file.type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
        doc = docx.Document(uploaded_file)
        extracted_text = '\n'.join([para.text for para in doc.paragraphs])

    st.write("Extracted text:", extracted_text[:100] + "...")
    detected_lang = detect(extracted_text)

    target_lang_doc = st.selectbox("Select target language for document:", [
        'english', 'spanish', 'french', 'german', 'italian', 
        'arabic', 'hindi', 'portuguese', 'russian', 'japanese', 
        'korean', 'bengali', 'turkish', 'amharic'
    ], key="doc_lang")

    if st.button("Translate Document up to 10,000 characters"):
        translated_doc_text = GoogleTranslator(target=target_lang_doc).translate(text=extracted_text)
        st.write(f"Translated document text: {translated_doc_text[:10000]}...")
