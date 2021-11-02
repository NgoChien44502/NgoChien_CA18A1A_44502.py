"""
Dề thi 2
Date: 29/10/2000
Ngo Van Chien
"""
def Cau2():
    data = []
    n = 0

    class Mathang:
        def __init__(self, ma, ten, sl, dg) -> None:
            self.ma_mat_hang = ma
            self.ten_mat_hang = ten
            self.so_luong = sl
            self.don_gia = dg

        @property
        def thanh_tien(self):
            return self.so_luong * self.don_gia

    def cv23():

        f = open("CA18A1A_Ngo Van Chien_44502_inp.txt", mode="r", encoding="utf-8")

        n = int(f.readline())
        for i in range(0, n):
            row_data = f.readline().split("|")
            mat_hang = Mathang(row_data[0], row_data[1], int(row_data[2]), int(row_data[3]))
            data.append(mat_hang)

        f.close()
        print("=="*10)
        print("Hoàn thành nhập dữ liệu từ file: CA18A1A_Ngo Van Chien_44502_inp.txt ")

    def cv24():
        print("=="*20)
        if len(data) == 0:
            print("bạn cần nhập thông tin mặt hàng")
        else:
            print("\nThong tin về mặt hàng:\n")
            print("==" * 20)
            for i in data:
                print("{:<5} {:<15} {:>5} {:>10} {:>10}" \
                      .format(i.ma_mat_hang, i.ten_mat_hang, i.so_luong, i.don_gia, i.thanh_tien))
        print("==" * 20)

    def cv25():
        if len(data) == 0:
            print("Bạn cần nhập thông tin mặt hàng")
        else:
            f = open("CA18A1A_Ngo Van Chien_44502_out.txt", mode="w", encoding="utf-8")
            f.write(str(len(data)) + "\n")
            for i in data:
                s = i.ma_mat_hang + "|" + i.ten_mat_hang + "|" + str(i.so_luong) \
                     + "|" + str(i.don_gia) + "|" +str(i.thanh_tien) + "\n"
                f.write(s)
            f.close()
        print("Hoàn thành in file: CA18A1A_Ngo Van Chien_44502_out.txt")
        print(("++"*20))
    def cau25():
        print("=="*20)
        mathangdai = data[0]
        for i in data:
            if i.don_gia > mathangdai.don_gia:
                mathangdai = i
        mathangdai_str = mathangdai.ma_mat_hang + "|" + mathangdai.ten_mat_hang + "|" + str(mathangdai.so_luong) \
            + "|" + str(mathangdai.don_gia) + "|" + str(mathangdai.thanh_tien) + "\n"
        print(mathangdai_str)
        print("=="*20)


    while True:
            print("---MENU---")
            print("2.3. Nhập dữ liệu")
            print("2.4. In dữ liệu")
            print("2.5. In mặt hàng với đơn gia slowns nhất")
            print("2.5. Ghi thông tin")
            cv = input("bạn chon cv, bấm K đê thoát:")
            if cv == "1":
                print("call cv23")
                cv23()
            elif cv == "2":
                cv24()
            elif cv == "25":
                cau25()
            elif cv == "3":
                cv25()
            elif cv.upper() == "K":
                break

if __name__ == '__main__':
    Cau2()






