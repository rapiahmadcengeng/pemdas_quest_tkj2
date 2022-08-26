print("program bangun datar")

print("1.balok")

panjang = int(input("masukan nilai panjang: "))
lebar = int(input("masukan nilai lebar: "))
tinggi = int(input("masukan nilai tinggi: "))

volume_balok = panjang * lebar * tinggi
print("nilai volume balok", volume_balok)

print("2.\ntabung")
import math
r =float(input("masukan jari jari :"))
t =float(input("masukan tinggi :"))
pi =math. pi 
v =round(pi*(r*r)*t,2)
print("volume tabung adalah : ",v)

print("3.\nlimas")

alas = int(input("masukan nilai alas: "))
tinggi = int(input("masukan nilai tinggi: "))
volume_1= alas * tinggi
print("volume lumas adalah: ", volume_1)

kursDolar = 14000
rupiah = float(input("masukan nilai rupiah= "))
rupToDol = rupiah/ kursDolar
dolDecimal = round(rupToDol, 2)
print("rp.", rupiah, "==> US$", dolDecimal )






