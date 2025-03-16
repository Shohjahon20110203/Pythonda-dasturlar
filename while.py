# # 1) Foydalanuvchidan faqat to‘g‘ri parolni kiritishini talab qiluvchi dastur


parol = "python123"
kiritilgan_parol = ""

while kiritilgan_parol != parol:
    kiritilgan_parol = input("Parolni kiriting: ")
    if kiritilgan_parol != parol:
        print("Noto‘g‘ri parol! Qaytadan kiriting.")

print("Xush kelibsiz! ✅")




# 2) Son taxminlash o‘yini

import random

sirli_son = random.randint(1, 100)
taxmin = 0
urinishlar = 0

print("Men 1 dan 100 gacha son o‘yladim. Uni topishga harakat qiling!")

while taxmin != sirli_son:
    taxmin = int(input("Son kiriting: "))
    urinishlar += 1

    if taxmin > sirli_son:
        print("Xato! Men o‘ylagan son bundan kichik. 🔽")
    elif taxmin < sirli_son:
        print("Xato! Men o‘ylagan son bundan katta. 🔼")

print(f"Tabriklayman! 🎉 Siz {urinishlar} ta urinishda topdingiz.")



# 3) Cheksiz kalkulyator



while True:
    amal = input("Amalni kiriting (+, -, *, / yoki 'exit' chiqish uchun): ")

    if amal == "exit":
        print("Dastur tugadi! ✅")
        break

    son1 = float(input("Birinchi sonni kiriting: "))
    son2 = float(input("Ikkinchi sonni kiriting: "))

    if amal == "+":
        print(f"Natija: {son1 + son2}")
    elif amal == "-":
        print(f"Natija: {son1 - son2}")
    elif amal == "*":
        print(f"Natija: {son1 * son2}")
    elif amal == "/":
        if son2 != 0:
            print(f"Natija: {son1 / son2}")
        else:
            print("Nolga bo‘lish mumkin emas! ❌")
    else:
        print("Noto‘g‘ri amal kiritildi! 🚫")



# 4) Foydalanuvchi faqat musbat son kiritishi kerak


while True:
    son = int(input("Musbat son kiriting (0 yoki manfiy son kiritsangiz, dastur tugaydi): "))

    if son <= 0:
        print("Dastur tugadi! ✅")
        break
    else:
        print(f"Siz {son} kiritdingiz. Davom eting!")



# 5)  1 dan N gacha bo‘lgan sonlar yig‘indisini hisoblash


n = int(input("N ni kiriting: "))
summa = 0
i = 1

while i <= n:
    summa += i
    i += 1

print(f"1 dan {n} gacha bo‘lgan sonlar yig‘indisi: {summa}")



# 6) Foydalanuvchi kiritgan raqamning raqamlari yig‘indisini hisoblash

son = int(input("Sonni kiriting: "))
summa = 0

while son > 0:
    raqam = son % 10  # Oxirgi raqamni ajratib olamiz
    summa += raqam  # Raqamni yig‘indiga qo‘shamiz
    son //= 10  # Sonni qisqartiramiz

print(f"Raqamlar yig‘indisi: {summa}")


# 7) Fibonacci ketma-ketligini chiqarish


n = int(input("Nechta Fibonacci soni chiqarilsin? "))

a, b = 0, 1
i = 0

while i < n:
    print(a, end=" ")
    a, b = b, a + b
    i += 1



# 8) Mukammal sonni tekshirish


son = int(input("Mukammal sonni tekshirish uchun son kiriting: "))

yigindi = 0
i = 1

while i < son:
    if son % i == 0:
        yigindi += i
    i += 1

if yigindi == son:
    print(f"{son} mukammal son! ✅")
else:
    print(f"{son} mukammal son emas. ❌")

# 9) Son teskari yozish dasturi


son = int(input("Son kiriting: "))
teskari_son = 0

while son > 0:
    qoldiq = son % 10
    teskari_son = teskari_son * 10 + qoldiq
    son //= 10

print(f"Teskari son: {teskari_son}")

# 10) Ikki sonning EKUB (eng katta umumiy bo‘luvchi) ni topish



a = int(input("Birinchi sonni kiriting: "))
b = int(input("Ikkinchi sonni kiriting: "))

while b != 0:
    a, b = b, a % b  # Evklid algoritmi

print(f"EKUB: {a}")
