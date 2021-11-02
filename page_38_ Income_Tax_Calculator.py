"""
Author: Ngo Van Chien
Date: 03/09/2021

Problem:   Case Study: Income Tax Calculator
        Most of the chapters in this book include a case study that illustrates the software
        development process. This approach may seem overly elaborate for small programs,
        but it scales up well when programs become larger. The first case study develops a
        program that calculates income tax.
        Each year, nearly everyone with an income faces the unpleasant task of computing
        his or her income tax return. If only it could be done as easily as suggested in this
        case study! We start with the customer request phase.
        Request
        The customer requests a program that computes a person’s income tax.
        Analysis
        Analysis often requires the programmer to learn some things about the problem
        domain, in this case, the relevant tax law. For the sake of simplicity, let’s assume the
        following tax laws:
        • All taxpayers are charged a flat tax rate of 20%.
        • All taxpayers are allowed a $10,000 standard deduction.
        • For each dependent, a taxpayer is allowed an additional $3,000 deduction.
        • Gross income must be entered to the nearest penny.
        • The income tax is expressed as a decimal number.
        Another part of analysis determines what information the user will have to provide.
        In this case, the user inputs are gross income and number of dependents. The
        program calculates the income tax based on the inputs and the tax law and then
        displays the income tax. Figure 2-4 shows the proposed terminal-based interface.
        Characters in italics indicate user inputs. The program prints the rest. The inclusion
        of an interface at this point is a good idea because it allows the customer and the
        programmer to discuss the intended program’s behavior in a context understandable to both.

Solution:
        Thiết kế
    Trong quá trình phân tích,  chỉ rõ chương trình sẽ làm gì.

    Nhập tổng thu nhập và số người phụ thuộc
    Tính thu nhập chịu thuế theo công thức
    thu nhập chịu thuế = tổng thu nhập- 10000- (3000 * số người phụ thuộc)
    Tính thuế bằng công thức
    thuế = thu nhập chịu thuế * 0,2
    in thuế
        Triển khai (Mã hóa)

    Khai thuế thu nhập của một người.
    1. hằng số quan trọng
        thuế suất
        khấu trừ tiêu chuẩn
        khấu trừ cho mỗi người phụ thuộc
    2. các đầu vào là
        Tổng thu nhập
        số người phụ thuộc
    3. tính toán
        thu nhập chịu thuế = tổng thu nhập - khoản khấu trừ tiêu chuẩn - khoản giảm trừ cho từng người phụ thuộc
        thuế thu nhập = là tỷ lệ phần trăm cố định của thu nhập chịu thuế
    4. đầu ra là
        thuế thu nhập

    ....
"""
thuesuat = 0.2
khautrutieuchuan = 10000
khautrunguoiphuthuoc = 3000

tongthunhap = float(input("Nhập tổng thu nhập:"))
songuoiphuthuoc = int(input("Nhập số lượng người phụ thuộc:"))

thunhapchiuthue = tongthunhap-khautrutieuchuan-khautrunguoiphuthuoc*songuoiphuthuoc
thuethunhap = thunhapchiuthue*thuesuat

print("Thuế thu nhập là $ :",thuethunhap)





