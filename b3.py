patient_name = input("Nhập tên bệnh nhân: ")
patient_age = int(input("Nhập tuổi bệnh nhân: "))
result_classify = ""

if (patient_age > 150 or patient_age < 1) or patient_name.strip() == "":
    print("LỖI: Tên không hợp lệ hoặc Tuổi nằm ngoài phạm vi con người (0-150)!")
else:     
    if patient_age < 6:
        result_classify = "ƯU TIÊN: Bệnh nhi - Chuyển thẳng phòng khám Nhi."
    elif patient_age >= 80:
        result_classify = "ƯU TIÊN: Người cao tuổi - Hỗ trợ xe lăn, chuyển phòng khám Lão khoa."
    else:
        result_classify = "KHÁM THƯỜNG: Vui lòng lấy số thứ tự và chờ tới lượt tại sảnh."
    print("----- PHIẾU KHÁM BỆNH -----")
    print(f"Tên: {patient_name}")
    print(f"Tuổi: {patient_age}")
    print(f"Kết quả: {result_classify}")