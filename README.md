# 🌐 Language Translation App

## Overview

The **Language Translation App** is a powerful and user-friendly application built using Streamlit that allows users to translate both text input and documents (PDF or Word). It leverages the Deep Translator library for translation, Google Text-to-Speech (gTTS) for voice synthesis, and PyPDF2 and python-docx libraries for extracting text from PDF and DOCX files. The app also supports language detection using `langdetect`.

## Features

- **Text Translation**: Translate text input to various languages.
- **Document Translation**: Upload PDF or DOCX files and translate up to 10,000 characters.
- **Language Detection**: Automatically detect the source language of the input text.
- **File Types Supported**: PDF and DOCX for document translation.
- **Custom UI Styling**: Modern, slick design using custom CSS for enhanced user experience.

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/nathe444/language-translation-langchain.git
    cd language-translation-langchain
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Required Packages

The application relies on the following libraries:

- **Streamlit**: For creating the web interface.
- **Deep Translator**: For performing text translations.
- **gTTS**: For generating text-to-speech audio.
- **PyPDF2**: For extracting text from PDF files.
- **python-docx**: For extracting text from Word documents.
- **langdetect**: For detecting the input language automatically.

To install these packages manually, you can run:

```bash
pip install streamlit deep-translator gTTS PyPDF2 python-docx langdetect

```

## Contact
Email - natnaelm552@gmail.com
