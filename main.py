# Hàm giới thiệu và hiển thị danh sách sản phẩm
def gioithieu():
    print("Chào mừng bạn đến với ứng dụng bán điện thoại của chúng tôi")
    print("Chúng tôi cung cấp các sản phẩm chất lượng với giá cả hợp lý")
    print("Hãy chọn sản phẩm bạn muốn mua")
    # Tạo danh sách sản phẩm dạng bảng
    print("Danh sách sản phẩm")
    print("STT\tTên sản phẩm\tGiá")
    print("1\tĐiện thoại Samsung Galaxy A50\t6.990.000")
    print("2\tĐiện thoại Samsung Galaxy A70\t8.990.000")
    print("3\tĐiện thoại Samsung Galaxy A80\t12.990.000")
    print("4\tĐiện thoại Samsung Galaxy S10\t15.990.000")
    print("5\tĐiện thoại Samsung Galaxy Note 10\t22.990.000")
    print("6\tĐiện thoại Samsung Galaxy Note 10+\t25.990.000")
    print("7\tĐiện thoại Samsung Galaxy Fold\t50.990.000")
    print("8\tĐiện thoại Samsung Galaxy S20\t20.990.000")
    print("9\tĐiện thoại Samsung Galaxy S20+\t24.990.000")
    print("10\tĐiện thoại Samsung Galaxy S20 Ultra\t29.990.000")

# Vòng lặp chính để người dùng có thể mua nhiều lần
while True:
    gioithieu()  # Hiển thị thông tin sản phẩm

    # Nhập số thứ tự sản phẩm
    stt = int(input("Nhập số thứ tự sản phẩm bạn muốn mua: "))

    # Nhập số lượng sản phẩm
    soluong = int(input("Nhập số lượng sản phẩm bạn muốn mua: "))

    # Tính tổng tiền dựa trên số thứ tự sản phẩm
    if stt == 1:
        tongtien = soluong * 6990000
    elif stt == 2:
        tongtien = soluong * 8990000
    elif stt == 3:
        tongtien = soluong * 12990000
    elif stt == 4:
        tongtien = soluong * 15990000
    elif stt == 5:
        tongtien = soluong * 22990000
    elif stt == 6:
        tongtien = soluong * 25990000
    elif stt == 7:
        tongtien = soluong * 50990000
    elif stt == 8:
        tongtien = soluong * 20990000
    elif stt == 9:
        tongtien = soluong * 24990000
    elif stt == 10:
        tongtien = soluong * 29990000

    # Hiển thị tổng tiền
    print("Tổng tiền bạn phải trả là: ", tongtien)

    # Nhập thông tin khách hàng
    ten = input("Nhập họ tên của bạn: ")
    diachi = input("Nhập địa chỉ của bạn: ")
    sdt = input("Nhập số điện thoại của bạn: ")

    # Hiển thị thông tin đơn hàng
    print("Cảm ơn bạn đã mua hàng của chúng tôi")
    print("Thông tin đơn hàng của bạn")
    print("Họ tên: ", ten)
    print("Địa chỉ: ", diachi)
    print("Số điện thoại: ", sdt)
    print("Sản phẩm đã mua")
    if stt == 1:
        print("Điện thoại Samsung Galaxy A50")
    elif stt == 2:
        print("Điện thoại Samsung Galaxy A70")
    elif stt == 3:
        print("Điện thoại Samsung Galaxy A80")
    elif stt == 4:
        print("Điện thoại Samsung Galaxy S10")
    elif stt == 5:
        print("Điện thoại Samsung Galaxy Note 10")
    elif stt == 6:
        print("Điện thoại Samsung Galaxy Note 10+")
    elif stt == 7:
        print("Điện thoại Samsung Galaxy Fold")
    elif stt == 8:
        print("Điện thoại Samsung Galaxy S20")
    elif stt == 9:
        print("Điện thoại Samsung Galaxy S20+")
    elif stt == 10:
        print("Điện thoại Samsung Galaxy S20 Ultra")
    print("Số lượng: ", soluong)
    print("Tổng tiền: ", tongtien)

    # Hỏi người dùng có muốn mua tiếp không
    tieptuc = input("Bạn có muốn mua tiếp không (có/không)? ")
    if tieptuc.lower() == "không":
        print("Cảm ơn bạn đã sử dụng dịch vụ của chúng tôi")
        break
    elif tieptuc.lower() == "có":
        continue
    else:
        print("Lựa chọn không hợp lệ")
        break
