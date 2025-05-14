
import streamlit as st
import sys
import os
sys.path.append(os.path.dirname(__file__))

from utils.extract import extract_content
from utils.process import generate_quy_trinh_context
from utils.flowchart import generate_flowchart
from utils.word_export import export_to_word

st.title("🤖 Chatbot Soạn Quy Trình Tự Động")

uploaded_file = st.file_uploader("📥 Tải file mẫu (PDF, DOCX)", type=["pdf", "docx"])

if uploaded_file:
    raw_text = extract_content(uploaded_file)
    st.text_area("📄 Nội dung đã trích xuất", raw_text, height=200)

    if st.button("🔄 Tạo Quy Trình Chuẩn"):
        context = generate_quy_trinh_context(raw_text)
        flowchart_path = generate_flowchart(context["steps"])
        docx_path = export_to_word(context, flowchart_path)

        with open(docx_path, "rb") as f:
            st.download_button("📥 Tải file quy trình hoàn chỉnh", f, file_name="quy_trinh.docx")
