import os
from PyPDF2 import PdfReader
from docx import Document
import streamlit as st

def pdf_to_word(pdf_file):
    # Check file size
    if pdf_file.size > 5 * 1024 * 1024:  # 5MB in bytes
        st.error("File is larger than 5MB. Please choose a smaller file.")
        return None

    # Read PDF
    pdf = PdfReader(pdf_file)
    
    # Create a new Word document
    doc = Document()

    # Iterate through pages and extract text
    for page in pdf.pages:
        text = page.extract_text()
        doc.add_paragraph(text)

    # Save the Word document
    output_path = "converted_document.docx"
    doc.save(output_path)
    return output_path

st.title("PDF to Word Converter")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    if st.button("Convert to Word"):
        with st.spinner("Converting..."):
            output_file = pdf_to_word(uploaded_file)
        
        if output_file:
            st.success("Conversion successful!")
            with open(output_file, "rb") as file:
                st.download_button(
                    label="Download Word document",
                    data=file,
                    file_name="converted_document.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )
