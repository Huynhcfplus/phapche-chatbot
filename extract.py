
import docx2txt
import PyPDF2

def extract_content(uploaded_file):
    if uploaded_file.name.endswith(".docx"):
        return docx2txt.process(uploaded_file)
    elif uploaded_file.name.endswith(".pdf"):
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        return "\n".join([page.extract_text() for page in pdf_reader.pages])
    return ""
