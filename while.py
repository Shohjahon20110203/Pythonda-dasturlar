# # 1) Foydalanuvchidan faqat to‘g‘ri parolni kiritishini talab qiluvchi dastur


# parol = "python123"
# kiritilgan_parol = ""

# while kiritilgan_parol != parol:
#     kiritilgan_parol = input("Parolni kiriting: ")
#     if kiritilgan_parol != parol:
#         print("Noto‘g‘ri parol! Qaytadan kiriting.")

# print("Xush kelibsiz! ✅")




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
