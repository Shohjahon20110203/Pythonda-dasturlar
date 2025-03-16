# 1) Sonning faktorialini hisoblovchi funksiya


def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

n = int(input("Sonni kiriting: "))
print(f"{n}! = {faktorial(n)}")



# 2) Son teskari yoziladigan funksiya


def teskari_son(son):
    teskari = 0
    while son > 0:
        qoldiq = son % 10
        teskari = teskari * 10 + qoldiq
        son //= 10
    return teskari

n = int(input("Son kiriting: "))
print(f"Teskari yozilgan son: {teskari_son(n)}")



# 3) Foydalanuvchi kiritgan son tub yoki yo‘qligini tekshiruvchi funksiya


def tubmi(son):
    if son < 2:
        return False
    for i in range(2, int(son ** 0.5) + 1):
        if son % i == 0:
            return False
    return True

n = int(input("Son kiriting: "))
if tubmi(n):
    print(f"{n} - tub son! ✅")
else:
    print(f"{n} - tub son emas. ❌")



# 4) Ikki sonning EKUB (Eng Katta Umumiy Bo‘luvchi) ni topish


def ekub(a, b):
    while b:
        a, b = b, a % b
    return a

x = int(input("Birinchi sonni kiriting: "))
y = int(input("Ikkinchi sonni kiriting: "))
print(f"{x} va {y} ning EKUB: {ekub(x, y)}")



# 5) Ikki sonning EKUK (Eng Kichik Umumiy Ko‘paytuvchi) ni topish


def ekuk(a, b):
    return (a * b) // ekub(a, b)  # EKUK = (a * b) / EKUB

x = int(input("Birinchi sonni kiriting: "))
y = int(input("Ikkinchi sonni kiriting: "))
print(f"{x} va {y} ning EKUK: {ekuk(x, y)}")



# 6) Foydalanuvchi kiritgan sonning raqamlari yig‘indisini hisoblovchi funksiya



def raqamlar_yigindisi(son):
    yigindi = 0
    while son > 0:
        yigindi += son % 10
        son //= 10
    return yigindi

n = int(input("Son kiriting: "))
print(f"Raqamlar yig‘indisi: {raqamlar_yigindisi(n)}")



# 7)  Fibonacci ketma-ketligini hisoblash (rekursiv funksiya)


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Nechta Fibonacci soni chiqarilsin? "))
for i in range(n):
    print(fibonacci(i), end=" ")



# 8) So‘zdagi unli harflar sonini hisoblovchi funksiya      


def unli_harf_soni(matn):
    unlilar = "aoueiAOUEI"
    sanash = sum(1 for harf in matn if harf in unlilar)
    return sanash

so‘z = input("So‘z kiriting: ")
print(f"Unli harflar soni: {unli_harf_soni(so‘z)}")



# 9) Berilgan son mukammal son ekanligini aniqlovchi funksiya


def mukammalmi(son):
    yigindi = sum(i for i in range(1, son) if son % i == 0)
    return yigindi == son

n = int(input("Mukammal sonni tekshirish uchun son kiriting: "))
if mukammalmi(n):
    print(f"{n} mukammal son! ✅")
else:
    print(f"{n} mukammal son emas. ❌")



# 10) Berilgan sonni teskari o‘girib palindrom ekanligini tekshiruvchi funksiya

def palindrommi(son):
    return str(son) == str(son)[::-1]

n = int(input("Son kiriting: "))
if palindrommi(n):
    print(f"{n} palindrom son! ✅")
else:
    print(f"{n} palindrom son emas. ❌")



# 11) 