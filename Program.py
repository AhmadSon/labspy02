#program mencari bilangan terbesar dari 3 buah bilangan
a = int(input("Masukkan bilangan A:"))
b = int(input("Masukkan bilangan B:"))
c = int(input("Masukkan bilangan C:"))

if a > b and a > c:
    print("A yang terbesar")
elif b > a and b > c:
    print("B yang terbesar")
else:
    print("C yang terbesar")