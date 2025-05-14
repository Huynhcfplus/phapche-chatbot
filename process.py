
def generate_quy_trinh_context(raw_text):
    return {
        "ten_quy_trinh": "Quy trình xử lý hồ sơ",
        "muc_dich": "Đảm bảo đúng tiến độ và tuân thủ quy định",
        "pham_vi": "Áp dụng toàn công ty",
        "co_so_phap_ly": "Căn cứ theo Luật...",
        "noi_dung": raw_text,
        "trach_nhiem": "P.HCNS chủ trì, các phòng phối hợp",
        "bieu_mau": "- Mẫu tiếp nhận\n- Mẫu xử lý",
        "hieu_luc": "Từ ngày ký",
        "nguoi_lap": "Nguyễn Văn A",
        "nguoi_duyet": "Trần Văn B",
        "steps": [
            ("Tiếp nhận hồ sơ", "Kiểm tra hồ sơ"),
            ("Kiểm tra hồ sơ", "Phê duyệt"),
            ("Phê duyệt", "Lưu trữ")
        ]
    }
