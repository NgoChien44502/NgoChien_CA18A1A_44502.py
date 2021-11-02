"""
Ôn tập 2
Date: 29/10/2000
Ngo Van Chien
"""
def Cau2():
    data = [] # list chua cac doi tuong
    n = 0 # so luong mat hang

    class MatHang:
        def __init__(self, ma, ten, sl, dg) -> None:
            self.ma_thiet_bi = ma
            self.ten_mat_hang = ten
            self.so_luong = sl
            self.don_gia = dg

        @property
        def thanh_tien(self):
            return self.so_luong * self.don_gia

    def cv23():

        # mo file
        f = open("CA18A1A_Ngo Van Chien_44502_inp.txt", mode="r", encoding="utf-8")

        # doc du lieu va dua vao class
        n = int(f.readline()) # n la so luong mat hang

        for i in range(0, n):
            row_data = f.readline().split("|")
            mat_hang = MatHang(row_data[0], row_data[1], int(row_data[2]), int(row_data[3]))
            data.append(mat_hang) # dua du lieu vao data cac object

        # dong file
        f.close()
        print("=="*20)
        print(" ==> Hoan thanh viec nhap du lieu tu file: CA18A1A_Ngo Van Chien_44502_inp.txt")

    def cv24():
        print("==" * 20)
        if len(data) == 0:
            print(" ban can nhap thong tin ve mat hang")
        else:
            # da co thong tin, xu ly
            print("\nIn thong tin cac mat hang:\n")
            for i in data:
                print("{:<5} {:<15} {:>5} {:>10} {:>10}" \
                      .format(i.ma_thiet_bi, i.ten_mat_hang, i.so_luong, i.don_gia, i.thanh_tien))
        print("=="*20)

    def cv25():
        """ hien thi mat hang co don gia cao nhat """
        print("=="*20)
        MatHangDatNhat = data[0]
        for i in data:
            if i.don_gia > MatHangDatNhat.don_gia:
                MatHangDatNhat = i
        MatHangDatNhat_str = MatHangDatNhat.ma_thiet_bi + "|" + MatHangDatNhat.ten_mat_hang + "|" + str(MatHangDatNhat.so_luong) \
            + "|" + str(MatHangDatNhat.don_gia) + "|" + str(MatHangDatNhat.thanh_tien) + "\n"
        print(MatHangDatNhat_str)
        print("==" * 20)

    def cv26():
        if len(data) == 0:
            print(" ban can nhap thong tin ve mat hang")
        else:
            # ghi du lieu
            f = open("CA18A1A_Ngo Van Chien_44502_out.txt", mode="w", encoding="utf-8")

            f.write(str(len(data)) + "\n")

            for i in data:
                s = i.ma_thiet_bi + "|" + i.ten_mat_hang + "|" + str(i.so_luong) \
                    + "|" + str(i.don_gia) + "|" + str(i.thanh_tien) + "\n"
                f.write(s)

            f.close()
        print("hoan thanh ghi ra file: CA18A1A_Ngo Van Chien_44502_out.txt")
        print("=="*20)

    while True:
        print("---MENU---")
        print("1. nhap du lieu .")
        print("2. in du lieu ra man hinh.")
        print("3. in mat hang don gia cao nhat.")
        print("4. ghi thong tin.")
        cv = input(" Ban chon cong viec, bam K de thoat: ")
        if cv == "1":
            cv23()
        elif cv == "2":
            cv24()
        elif cv == "3":
            cv25()
        elif cv == "4":
            cv26()
        elif cv.upper() == "K":
            break


if __name__ == '__main__':
    Cau2()
