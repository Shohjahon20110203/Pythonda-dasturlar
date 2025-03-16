# 1) Son musbat yoki manfiyligini aniqlash

# Tavsif: Foydalanuvchi kiritgan son musbat, manfiy yoki nol ekanligini aniqlaydi.

son = int(input("Istalgan son kiriting: "))

if son > 0:
    print("Bu musbat son.")
elif son < 0:
    print("Bu manfiy son.")
else:
    print("Bu nol.")





# 2)  Juft yoki toq son aniqlash

# Tavsif: Foydalanuvchi kiritgan son juft yoki toq ekanligini tekshiradi.

son = int(input("Istalgan son kiriting: "))

if son % 2 == 0:
    print("Bu juft son.")
else:
    print("Bu toq son.")


# 3)  Bankomat dasturi (Pul yechish)



# Bankdagi hisob
hisob = {
    "Ali": 500000,
    "Vali": 1200000,
    "Olim": 300000
}

ism = input("Ismingizni kiriting: ")

if ism in hisob:
    summa = int(input("Qancha pul yechmoqchisiz? "))
    
    if summa > hisob[ism]:
        print("Hisobingizda yetarli mablag‘ yo‘q! ❌")
    else:
        hisob[ism] -= summa
        print(f"{summa} so‘m yechildi. Hisobingizda {hisob[ism]} so‘m qoldi. ✅")
else:
    print("Sizning hisobingiz mavjud emas! 🚫")



# 4) Onlayn do‘kon (Chegirma tizimi)



# Mijoz ma’lumotlari
mijozlar = {
    "Ali": True,
    "Vali": False,
    "Olim": True
}

# Minimal chegirma olish summasi
min_chegirma_summa = 200000

ism = input("Ismingizni kiriting: ")
buyurtma_summa = int(input("Buyurtma summasini kiriting: "))

if ism in mijozlar:
    chegirma = 0

    if mijozlar[ism]:  # Doimiy mijozmi?
        chegirma = 10  # 10% chegirma
    elif buyurtma_summa > min_chegirma_summa:
        chegirma = 5  # 5% chegirma
    
    if chegirma > 0:
        yakuniy_summa = buyurtma_summa - (buyurtma_summa * chegirma / 100)
        print(f"Sizga {chegirma}% chegirma berildi! To‘lanishi kerak bo‘lgan summa: {yakuniy_summa} so‘m.")
    else:
        print("Sizga chegirma berilmadi. To‘lanishi kerak bo‘lgan summa:", buyurtma_summa)
else:
    print("Siz do‘konda ro‘yxatdan o‘tmagansiz! 🚫")




# 5) Uchburchak turini aniqlash


a = int(input("Birinchi tomon uzunligini kiriting: "))
b = int(input("Ikkinchi tomon uzunligini kiriting: "))
c = int(input("Uchinchi tomon uzunligini kiriting: "))

if a + b > c and a + c > b and b + c > a:  # Uchburchak sharti
    if a == b == c:
        print("Bu teng tomonli uchburchak.")
    elif a == b or a == c or b == c:
        print("Bu teng yonli uchburchak.")
    else:
        print("Bu turli tomonli uchburchak.")
else:
    print("Bunday uchburchak mavjud emas!")


# 6)  Login va parol tekshirish (Murakkab tizim)

foydalanuvchilar = {
    "ali": "1234",
    "vali": "abcd",
    "olim": "pass123"
}

login = input("Login kiriting: ").lower()
urinishlar = 3  # Maksimal urinishlar soni

if login in foydalanuvchilar:
    while urinishlar > 0:
        parol = input("Parolni kiriting: ")
        if parol == foydalanuvchilar[login]:
            print("Muvaffaqiyatli tizimga kirdingiz! ✅")
            break
        else:
            urinishlar -= 1
            print(f"Noto‘g‘ri parol! Qolgan urinishlar: {urinishlar}")
    else:
        print("Tizim bloklandi! 🚫")
else:
    print("Bunday foydalanuvchi mavjud emas!")




#  7) Imtihon natijalariga qarab stipendiya ajratish


baho1 = int(input("Birinchi fan bahosi: "))
baho2 = int(input("Ikkinchi fan bahosi: "))
baho3 = int(input("Uchinchi fan bahosi: "))
grant = input("Siz davlat granti asosidami? (ha/yo‘q): ").lower()

ortacha_baho = (baho1 + baho2 + baho3) / 3

if ortacha_baho >= 86 and grant == "ha":
    print("Siz stipendiya olasiz! 🎉")
elif ortacha_baho >= 86 and grant == "yo‘q":
    print("Siz faqat kontrakt asosida o‘qiysiz.")
else:
    print("Sizning baholaringiz stipendiya olish uchun yetarli emas.")




# 8)  Restoran menyusidan ovqat tanlash


menu = {
    "osh": 25000,
    "shashlik": 20000,
    "manti": 15000,
    "choy": 5000
}

buyurtma = input("Qaysi ovqatni buyurtma qilmoqchisiz? ").lower()

if buyurtma in menu:
    miqdor = int(input(f"{buyurtma.capitalize()} necha dona kerak? "))
    umumiy_narx = menu[buyurtma] * miqdor
    print(f"Jami summa: {umumiy_narx} so‘m")
else:
    print("Kechirasiz, bunday ovqat menyuda yo‘q! ❌")




# 9) 4 ta son ichidan eng kattasini topish

a = int(input("Birinchi sonni kiriting: "))
b = int(input("Ikkinchi sonni kiriting: "))
c = int(input("Uchinchi sonni kiriting: "))
d = int(input("To‘rtinchi sonni kiriting: "))

eng_katta = max(a, b, c, d)

print(f"Eng katta son: {eng_katta}")
