# pythonfrom datetime import datetime

class KhoaHoc:
    def __init__(self, ten_khoa_hoc, giao_vien, ngay_bat_dau, ngay_ket_thuc, so_sinh_vien, gia_khoa_hoc):
        self.ten_khoa_hoc = ten_khoa_hoc
        self.giao_vien = giao_vien
        self.ngay_bat_dau = ngay_bat_dau
        self.ngay_ket_thuc = ngay_ket_thuc
        self.so_sinh_vien = so_sinh_vien
        self.gia_khoa_hoc = gia_khoa_hoc

    def __str__(self):
        return (f"Tên khóa học: {self.ten_khoa_hoc}\n"
                f"  Giáo viên: {self.giao_vien}\n"
                f"  Ngày bắt đầu: {self.ngay_bat_dau}\n"
                f"  Ngày kết thúc: {self.ngay_ket_thuc}\n"
                f"  Số sinh viên: {self.so_sinh_vien}\n"
                f"  Giá khóa học: {self.gia_khoa_hoc:,.0f} VNĐ\n"
                f"------------------------------------")

class QuanLyKhoaHoc:
    def __init__(self):
        self.danh_sach_khoa_hoc = []

    def _lay_ngay_hop_le(self, prompt, current_date=None):
        while True:
            date_str = input(prompt)
            if current_date and not date_str:
                print(f"   >>> Giữ nguyên ngày cũ: {current_date}")
                return current_date
            
            try:
                if len(date_str) != 10 or date_str[2] != '/' or date_str[5] != '/':
                    raise ValueError("Định dạng ngày không đúng. Phải là DD/MM/YYYY.")
                
                parts = date_str.split('/')
                day = int(parts[0])
                month = int(parts[1])
                year = int(parts[2])

                if not (1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= 2100):
                    raise ValueError("Giá trị ngày, tháng hoặc năm không hợp lệ.")

                datetime.strptime(date_str, "%d/%m/%Y")
                return date_str
            except ValueError as e:
                print(f"   *** Lỗi: {e} Vui lòng nhập lại.")

    def _lay_so_nguyen_hop_le(self, prompt, min_val=0, max_val=999999999, current_val=None):
        while True:
            value_str = input(prompt)
            if current_val is not None and not value_str:
                print(f"   >>> Giữ nguyên giá trị cũ: {current_val}")
                return current_val
            
            try:
                value = int(value_str)
                if not (min_val <= value <= max_val):
                    print(f"   *** Lỗi: Giá trị phải là số nguyên trong khoảng từ {min_val} đến {max_val}. Vui lòng nhập lại.")
                else:
                    return value
            except ValueError:
                print("   *** Lỗi: Đầu vào không phải là số nguyên hợp lệ. Vui lòng nhập lại một số nguyên.")

    def _lay_so_thuc_hop_le(self, prompt, min_val=0.0, max_val=9999999999.0, current_val=None):
        while True:
            value_str = input(prompt)
            if current_val is not None and not value_str:
                print(f"   >>> Giữ nguyên giá trị cũ: {current_val:,.0f} VNĐ")
                return current_val
            
            try:
                value = float(value_str)
                if not (min_val <= value <= max_val):
                    print(f"   *** Lỗi: Giá trị phải là số (có thể có thập phân) trong khoảng từ {min_val:,.0f} đến {max_val:,.0f}. Vui lòng nhập lại.")
                else:
                    return value
            except ValueError:
                print("   *** Lỗi: Đầu vào không phải là số hợp lệ. Vui lòng nhập lại một số.")

    def them_khoa_hoc(self):
        print("\n--- Bắt đầu thêm Khóa học Mới ---")
        print("Vui lòng nhập các thông tin sau cho khóa học của bạn.")
        
        ten = input("1. Nhập TÊN khóa học (ví dụ: Lập trình Python3): ")
        gv = input("2. Nhập TÊN GIÁO VIÊN phụ trách: ")
        
        while True:
            nbd_str = self._lay_ngay_hop_le("3. Nhập NGÀY BẮT ĐẦU khóa học (DD/MM/YYYY, ví dụ: 01/07/2025): ")
            nkt_str = self._lay_ngay_hop_le("4. Nhập NGÀY KẾT THÚC khóa học (DD/MM/YYYY, ví dụ: 30/09/2025): ")
            
            try:
                nbd = datetime.strptime(nbd_str, "%d/%m/%Y")
                nkt = datetime.strptime(nkt_str, "%d/%m/%Y")
                
                if nbd > nkt:
                    print("   *** Lỗi: Ngày bắt đầu không thể diễn ra SAU ngày kết thúc. Vui lòng nhập lại cả hai ngày.")
                else:
                    break
            except ValueError:
                print("   *** Lỗi: Có vấn đề khi xử lý ngày. Vui lòng nhập lại ngày bắt đầu và ngày kết thúc.")

        sv = self._lay_so_nguyen_hop_le("5. Nhập SỐ SINH VIÊN tối đa đăng ký (chỉ nhập số, ví dụ: 50): ", min_val=0, max_val=1000)
        gia = self._lay_so_thuc_hop_le("6. Nhập GIÁ KHÓA HỌC (chỉ nhập số, ví dụ: 1500000): ", min_val=0.0, max_val=1000000000.0)

        khoa_hoc_moi = KhoaHoc(ten, gv, nbd_str, nkt_str, sv, gia)
        self.danh_sach_khoa_hoc.append(khoa_hoc_moi)
        print("\n>>> TUYỆT VỜI! Khóa học đã được THÊM thành công vào danh sách của bạn.")
        input("Nhấn Enter để tiếp tục...")

    def xem_khoa_hoc(self):
        if not self.danh_sach_khoa_hoc:
            print("\n--- Danh sách Khóa học ---")
            print("   Rất tiếc, hiện tại không có khóa học nào trong danh sách. Vui lòng thêm khóa học mới!")
            input("Nhấn Enter để tiếp tục...")
            return

        print("\n--- Danh sách các Khóa học hiện có ---")
        for i, kh in enumerate(self.danh_sach_khoa_hoc):
            print(f"Mã khóa học: {i+1}")
            print(kh)
        input("Nhấn Enter để tiếp tục xem menu chính...")

    def cap_nhat_khoa_hoc(self):
        self.xem_khoa_hoc()
        if not self.danh_sach_khoa_hoc:
            return

        print("\n--- Bắt đầu Cập nhật thông tin Khóa học ---")
        try:
            ma_kh = self._lay_so_nguyen_hop_le("Nhập MÃ SỐ khóa học bạn muốn cập nhật (ví dụ: 1): ", min_val=1, max_val=len(self.danh_sach_khoa_hoc)) - 1
            
            if 0 <= ma_kh < len(self.danh_sach_khoa_hoc):
                khoa_hoc = self.danh_sach_khoa_hoc[ma_kh]
                print(f"\nBạn đang cập nhật khóa học: '{khoa_hoc.ten_khoa_hoc}'.")
                print("Để GIỮ NGUYÊN thông tin cũ, hãy nhấn Enter (bỏ trống).")

                khoa_hoc.ten_khoa_hoc = input(f"1. Tên khóa học mới (hiện tại: {khoa_hoc.ten_khoa_hoc}): ") or khoa_hoc.ten_khoa_hoc
                khoa_hoc.giao_vien = input(f"2. Tên giáo viên mới (hiện tại: {khoa_hoc.giao_vien}): ") or khoa_hoc.giao_vien
                
                while True:
                    new_nbd_str = self._lay_ngay_hop_le(f"3. Ngày bắt đầu mới (hiện tại: {khoa_hoc.ngay_bat_dau}): ", current_date=khoa_hoc.ngay_bat_dau)
                    new_nkt_str = self._lay_ngay_hop_le(f"4. Ngày kết thúc mới (hiện tại: {khoa_hoc.ngay_ket_thuc}): ", current_date=khoa_hoc.ngay_ket_thuc)
                    
                    try:
                        nbd_obj = datetime.strptime(new_nbd_str, "%d/%m/%Y")
                        nkt_obj = datetime.strptime(new_nkt_str, "%d/%m/%Y")

                        if nbd_obj > nkt_obj:
                            print("   *** Lỗi: Ngày bắt đầu không thể sau ngày kết thúc. Vui lòng nhập lại cả hai ngày.")
                        else:
                            khoa_hoc.ngay_bat_dau = new_nbd_str
                            khoa_hoc.ngay_ket_thuc = new_nkt_str
                            break
                    except ValueError:
                        print("   *** Lỗi: Có vấn đề khi xử lý ngày. Vui lòng nhập lại ngày bắt đầu và ngày kết thúc.")

                khoa_hoc.so_sinh_vien = self._lay_so_nguyen_hop_le(
                    f"5. Số sinh viên mới (hiện tại: {khoa_hoc.so_sinh_vien}): ", 
                    min_val=0, max_val=1000, current_val=khoa_hoc.so_sinh_vien
                )
                khoa_hoc.gia_khoa_hoc = self._lay_so_thuc_hop_le(
                    f"6. Giá khóa học mới (hiện tại: {khoa_hoc.gia_khoa_hoc:,.0f} VNĐ): ", 
                    min_val=0.0, max_val=1000000000.0, current_val=khoa_hoc.gia_khoa_hoc
                )

                print("\n>>> XIN CHÚC MỪNG! Khóa học đã được CẬP NHẬT thành công!")
            else:
                print("   *** Lỗi: Mã khóa học bạn nhập không tồn tại. Vui lòng kiểm tra lại danh sách.")
        except ValueError:
            print("   *** Lỗi: Đầu vào không hợp lệ. Vui lòng nhập một SỐ cho mã khóa học.")
        input("Nhấn Enter để tiếp tục...")

    def xoa_khoa_hoc(self):
        self.xem_khoa_hoc()
        if not self.danh_sach_khoa_hoc:
            return

        print("\n--- Bắt đầu Xóa Khóa học ---")
        try:
            ma_kh_xoa = self._lay_so_nguyen_hop_le("Nhập MÃ SỐ khóa học bạn muốn xóa (ví dụ: 1): ", min_val=1, max_val=len(self.danh_sach_khoa_hoc)) - 1
            
            if 0 <= ma_kh_xoa < len(self.danh_sach_khoa_hoc):
                khoa_hoc_bi_xoa = self.danh_sach_khoa_hoc[ma_kh_xoa]
                
                xac_nhan = input(f"Bạn có chắc chắn muốn xóa khóa học '{khoa_hoc_bi_xoa.ten_khoa_hoc}' không? (gõ 'có' để xác nhận): ").lower()
                if xac_nhan == 'có':
                    self.danh_sach_khoa_hoc.pop(ma_kh_xoa)
                    print(f"\n>>> ĐÃ XÓA! Khóa học '{khoa_hoc_bi_xoa.ten_khoa_hoc}' đã được xóa thành công.")
                else:
                    print("\n>>> Hủy bỏ thao tác xóa. Khóa học vẫn còn trong danh sách.")
            else:
                print("   *** Lỗi: Mã khóa học bạn nhập không tồn tại trong danh sách.")
        except ValueError:
            print("   *** Lỗi: Đầu vào không hợp lệ. Vui lòng nhập một SỐ cho mã khóa học.")
        input("Nhấn Enter để tiếp tục...")

    def hien_thi_menu(self):
        print("\n===========================================")
        print("   HỆ THỐNG QUẢN LÝ KHÓA HỌC ĐƠN GIẢN")
        print("===========================================")
        print("1. Thêm khóa học mới")
        print("2. Xem tất cả khóa học hiện có")
        print("3. Cập nhật thông tin khóa học")
        print("4. Xóa một khóa học")
        print("5. Thoát khỏi chương trình")
        print("===========================================")

    def chay_chuong_trinh(self):
        print("Chào mừng bạn đến với Hệ thống Quản lý Khóa học!")
        while True:
            self.hien_thi_menu()
            lua_chon = input("Vui lòng nhập LỰA CHỌN của bạn (chỉ nhập số từ 1 đến 5): ")

            if lua_chon == '1':
                self.them_khoa_hoc()
            elif lua_chon == '2':
                self.xem_khoa_hoc()
            elif lua_chon == '3':
                self.cap_nhat_khoa_hoc()
            elif lua_chon == '4':
                self.xoa_khoa_hoc()
            elif lua_chon == '5':
                print("\nCảm ơn bạn đã sử dụng Hệ thống Quản lý Khóa học.")
                print("Chúc một ngày tốt lành! Hẹn gặp lại!")
                break
            else:
                print("\n   *** Lỗi: Lựa chọn của bạn không hợp lệ. Vui lòng chỉ nhập số từ 1 đến 5.")
                input("Nhấn Enter để thử lại...")

if __name__ == "__main__":
    qlkh = QuanLyKhoaHoc()
    qlkh.chay_chuong_trinh()
