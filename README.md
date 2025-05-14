
# 📄 Chatbot Pháp Chế (Legal Assistant Bot)

Một chatbot hỗ trợ soạn thảo văn bản pháp lý tự động, sử dụng mẫu `.docx` và tích hợp quy trình xử lý nội dung, biểu mẫu đầu vào.

---

## 🚀 Tính năng chính

- 📥 Nhận dữ liệu từ người dùng (file, biểu mẫu, text).
- ⚙️ Xử lý logic pháp chế và tạo văn bản theo mẫu.
- 📝 Xuất file Word hoàn chỉnh từ template.
- 📊 Vẽ sơ đồ quy trình pháp lý.
- ☁️ Dễ dàng triển khai trên Streamlit Cloud.

---

## 📁 Cấu trúc thư mục

```
phapche_chatbot_fixed/
├── app.py                    # Ứng dụng chính Streamlit
├── requirements.txt         # Thư viện cần thiết
├── templates/
│   └── quy_trinh_template.docx
└── utils/
    ├── extract.py
    ├── flowchart.py
    ├── process.py
    └── word_export.py
```

---

## 🧪 Cài đặt và chạy thử cục bộ

```bash
git clone https://github.com/ten-cua-ban/phapche_chatbot_fixed.git
cd phapche_chatbot_fixed
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

---

## ☁️ Triển khai trên Streamlit Cloud

1. Đưa toàn bộ mã nguồn lên GitHub.
2. Vào https://share.streamlit.io
3. Chọn repository và file `app.py`.
4. Nhấn **Deploy**.

---

## 💡 Gợi ý mở rộng

- Kết nối GPT API để hỗ trợ sinh nội dung thông minh.
- Lưu biểu mẫu theo mã để người dùng tái sử dụng.
- Trích xuất dữ liệu từ văn bản pháp luật (Thư viện Pháp luật, LuatVietnam, v.v).
- Giao diện thân thiện hơn với luồng hội thoại và lựa chọn nhanh.

---

## 📬 Liên hệ

Người phát triển: **[Tên của bạn]**  
Liên hệ: [email@example.com]
