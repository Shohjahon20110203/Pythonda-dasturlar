# 1. Dictionary yaratish

# Dictionary yaratish uchun {} jingalak qavslar yoki dict() funksiyasidan foydalaniladi.

mevalar = {"olma": "qizil", "banan": "sariq", "anor": "qizil"}
print(mevalar)



# 2. Dictionary'dan qiymat olish

# Kalit orqali mos qiymatni olish.

mevalar = {"olma": "qizil", "banan": "sariq", "anor": "qizil"}
rang = mevalar["banan"]
print(f"Banan rangi: {rang}")


# 3. Dictionary'ga yangi juftlik qoʻshish

# Dictionary'ga yangi kalit-qiymat juftligini qoʻshish.


mevalar = {"olma": "qizil", "banan": "sariq"}
mevalar["uzum"] = "qora"
print(mevalar)


# 4. Dictionary'dan elementni oʻchirish

# del yordamida dictionary'dan elementni oʻchirish.


mevalar = {"olma": "qizil", "banan": "sariq", "anor": "qizil"}
del mevalar["banan"]
print(mevalar)


# 5. Dictionary'dagi barcha kalitlarni olish

# .keys() metodi yordamida dictionary'dagi barcha kalitlarni olish.

mevalar = {"olma": "qizil", "banan": "sariq", "anor": "qizil"}
kalitlar = mevalar.keys()
print(f"Kalitlar: {kalitlar}")


# 6. Dictionary'dagi barcha qiymatlarni olish

# .values() metodi yordamida dictionary'dagi barcha qiymatlarni olish.


mevalar = {"olma": "qizil", "banan": "sariq", "anor": "qizil"}
qiymatlar = mevalar.values()
print(f"Qiymatlar: {qiymatlar}")



# 7. Dictionary'dagi barcha juftliklarni olish

# .items() metodi yordamida dictionary'dagi barcha kalit-qiymat juftliklarini olish.

mevalar = {"olma": "qizil", "banan": "sariq", "anor": "qizil"}
juftliklar = mevalar.items()
print(f"Juftliklar: {juftliklar}")



# 8. Dictionary'da kalit mavjudligini tekshirish

# Kalit dictionary'da mavjudligini tekshirish.


mevalar = {"olma": "qizil", "banan": "sariq", "anor": "qizil"}
if "olma" in mevalar:
    print("Olma mavjud")
else:
    print("Olma mavjud emas")


#  9. Dictionary'ni tozalash

# .clear() metodi yordamida dictionary'ni tozalash.

mevalar = {"olma": "qizil", "banan": "sariq", "anor": "qizil"}
mevalar.clear()
print(mevalar)


# 10. Dictionary'ni nusxalash   

# .copy() metodi yordamida dictionary'ni nusxalash.

mevalar = {"olma": "qizil", "banan": "sariq", "anor": "qizil"}
nusxa = mevalar.copy()
print(nusxa)

# 11. Dictionary'ni yangilash

# .update() metodi yordamida dictionary'ni yangilash.

mevalar = {"olma": "qizil", "banan": "sariq"}
mevalar.update({"anor": "qizil", "uzum": "qora"})
print(mevalar)


# 12. Dictionary'dan qiymatni olish va oʻchirish

# .pop() metodi yordamida qiymatni olish va uni dictionary'dan oʻchirish.


mevalar = {"olma": "qizil", "banan": "sariq", "anor": "qizil"}
rang = mevalar.pop("banan")
print(f"Oʻchirilgan qiymat: {rang}")
print(mevalar)


# 13. Dictionary'dan tasodifiy elementni olish va oʻchirish

# .popitem() metodi yordamida oxirgi qoʻshilgan elementni olish va uni dictionary'dan oʻchirish.

mevalar = {"olma": "qizil", "banan": "sariq", "anor": "qizil"}
oxirgi_element = mevalar.popitem()
print(f"Oʻchirilgan element: {oxirgi_element}")
print(mevalar)


# 14. Dictionary'da kalit boʻlmasa, standart qiymat qaytarish

# .get() metodi yordamida kalit boʻlmasa, standart qiymat qaytarish.

mevalar = {"olma": "qizil", "banan": "sariq", "anor": "qizil"}
rang = mevalar.get("uzum", "Nomaʼlum")
print(f"Uzum rangi: {rang}")


# 15. Dictionary'ni for tsikli bilan ishlatish

# Dictionary'ni for tsikli bilan ishlatish.


mevalar = {"olma": "qizil", "banan": "sariq", "anor": "qizil"}

for meva, rang in mevalar.items():
    print(f"{meva} rangi: {rang}")




















# Qiyin dasturlar top 20
 





# Talabalar baholari dasturi

# Tavsif: Talabalar va ularning baholarini saqlovchi dastur.


# 1) Talabalar baholari


baholar = {
    "Ali": 85,
    "Vali": 90,
    "Olim": 78,
    "Nodir": 92
}

# Talabaning bahosini chiqarish


ism = input("Talabaning ismini kiriting: ")
if ism in baholar:
    print(f"{ism}ning bahosi: {baholar[ism]}")
else:
    print("Bunday talaba topilmadi.")




# 2) Telefon kitobi

# Tavsif: Ismlar va ularning telefon raqamlarini saqlovchi lug‘at.



# Telefon kitobi
telefonlar = {
    "Ali": "+998901234567",
    "Vali": "+998977654321",
    "Olim": "+998935551122"
}

# Yangi kontakt qo'shish
ism = input("Yangi kontakt ismini kiriting: ")
raqam = input("Telefon raqamini kiriting: ")
telefonlar[ism] = raqam

print("\nYangilangan telefon kitobi:")
for k, v in telefonlar.items():
    print(f"{k}: {v}")




# 3) Valyuta konvertori

# Tavsif: Dollarni turli valyutalarga aylantiruvchi dastur

kurslar = {
    "EUR": 1.1,
    "RUB": 90,
    "UZS": 12500
}

# Dollarni boshqa valyutaga aylantirish
miqdor = float(input("Dollar miqdorini kiriting: "))
valyuta = input("Qaysi valyutaga (EUR, RUB, UZS) aylantirmoqchisiz? ").upper()

if valyuta in kurslar:
    natija = miqdor * kurslar[valyuta]
    print(f"{miqdor} USD = {natija} {valyuta}")
else:
    print("Bunday valyuta mavjud emas.")




# 4) So‘zlar lug‘ati (Tarjimon)

# Tavsif: So‘zlarni tarjima qiluvchi oddiy dastur.

# Tarjima lug‘ati
tarjimon = {
    "apple": "olma",
    "banana": "banan",
    "car": "mashina",
    "house": "uy"
}

# So‘zni tarjima qilish
soz = input("Tarjima qilmoqchi bo'lgan so‘zni kiriting: ").lower()

if soz in tarjimon:
    print(f"{soz} - {tarjimon[soz]}")
else:
    print("Bunday so‘z lug‘atda yo‘q.")




# 5) Mahsulotlar ombori (Do‘kon bazasi)

# Tavsif: Omborda mavjud mahsulotlar va ularning narxlarini saqlovchi dastur.

# Ombordagi mahsulotlar
mahsulotlar = {
    "non": 5000,
    "sut": 12000,
    "shakar": 15000,
    "choy": 8000
}

# Mahsulot narxini tekshirish
mahsulot = input("Mahsulot nomini kiriting: ").lower()

if mahsulot in mahsulotlar:
    print(f"{mahsulot.capitalize()} narxi: {mahsulotlar[mahsulot]} so'm")
else:
    print("Bunday mahsulot mavjud emas.")





# 6) Talabalar reytingi (Top talabalar)

# Tavsif: Talabalar va ularning ballari lug‘atda saqlanadi, eng yuqori ball olgan talabalar chiqariladi.



# Talabalar va ularning ballari
talabalar = {
    "Ali": 95,
    "Vali": 85,
    "Olim": 92,
    "Nodira": 98,
    "Sardor": 90
}

# Eng yaxshi talabani topish
eng_yaxshi = max(talabalar, key=talabalar.get)
print(f"Eng yuqori ball olgan talaba: {eng_yaxshi} ({talabalar[eng_yaxshi]} ball)")


# 7) Ish haqi hisoblash tizimi

# Tavsif: Xodimlarning maoshi saqlanadi va foydalanuvchi xodim nomini kiritganda uning maoshi ko‘rsatiladi.



# Xodimlar va ularning maoshi
ishchilar = {
    "Ali": 5000000,
    "Vali": 4500000,
    "Olim": 6000000,
    "Nodira": 7000000
}

# Xodim maoshini tekshirish
ism = input("Xodim ismini kiriting: ")

if ism in ishchilar:
    print(f"{ism}ning oyligi: {ishchilar[ism]} so'm")
else:
    print("Bunday xodim mavjud emas.")



# 8)  Shaxsiy kontaktlar ro‘yxati (Telefon kitobi)

# Tavsif: Kontaktlarni saqlash va yangi kontakt qo‘shish imkoniyati.



# Kontaktlar
kontaktlar = {
    "Ali": "+998901234567",
    "Vali": "+998977654321",
    "Olim": "+998935551122"
}

# Yangi kontakt qo‘shish
ism = input("Yangi kontakt ismini kiriting: ")
raqam = input("Telefon raqamini kiriting: ")

if ism in kontaktlar:
    print("Bu kontakt allaqachon mavjud.")
else:
    kontaktlar[ism] = raqam
    print(f"{ism} kontakt qo‘shildi!")

# Yangilangan kontaktlar ro‘yxati
print("\nYangilangan telefon kitobi:")
for k, v in kontaktlar.items():
    print(f"{k}: {v}")




# 9) Shaxsiy xarajatlarni hisoblash dasturi

# Tavsif: Foydalanuvchi har xil xarajatlarni kiritadi, dastur jami sarflangan pulni hisoblaydi.



# Xarajatlar lug‘ati
xarajatlar = {}

while True:
    mahsulot = input("Xarajat nomini kiriting (chiqish uchun 'stop'): ")
    if mahsulot.lower() == "stop":
        break
    narx = int(input(f"{mahsulot} narxini kiriting: "))
    xarajatlar[mahsulot] = narx

# Jami xarajatni hisoblash
jami = sum(xarajatlar.values())

print("\nSizning xarajatlaringiz:")
for mahsulot, narx in xarajatlar.items():
    print(f"{mahsulot}: {narx} so'm")

print(f"\nJami sarflangan summa: {jami} so'm")



# Harflar hisoblagich (Matndagi harflarni sanash)

# Tavsif: Foydalanuvchi matn kiritadi, dastur har bir harf necha marta qatnashganini lug‘atda saqlaydi.



# 10) Matndagi harflarni sanash
matn = input("Matn kiriting: ").lower()

harflar = {}
for harf in matn:
    if harf.isalpha():  # Faqat harflarni hisoblash
        harflar[harf] = harflar.get(harf, 0) + 1

# Natijani chiqarish
print("\nMatndagi harflar soni:")
for harf, soni in sorted(harflar.items()):
    print(f"{harf}: {soni}")








# 11) Foydalanuvchi profillari (Shaxsiy ma'lumotlar saqlash)

# Tavsif: Foydalanuvchilarning shaxsiy ma'lumotlarini saqlovchi dastur.


# Foydalanuvchilar ma'lumotlari
foydalanuvchilar = {
    "ali": {"ism": "Ali Valiyev", "yosh": 25, "email": "ali@gmail.com"},
    "vali": {"ism": "Vali Karimov", "yosh": 30, "email": "vali@gmail.com"}
}

# Foydalanuvchi ma'lumotlarini ko'rsatish
login = input("Foydalanuvchi loginini kiriting: ").lower()

if login in foydalanuvchilar:
    foydalanuvchi = foydalanuvchilar[login]
    print(f"Ism: {foydalanuvchi['ism']}\nYosh: {foydalanuvchi['yosh']}\nEmail: {foydalanuvchi['email']}")
else:
    print("Bunday foydalanuvchi topilmadi.")






# 12) Shopping Cart (Xarid qilish savatchasi)

# Tavsif: Foydalanuvchi mahsulotlarni savatchaga qo'shib, jami narxni hisoblaydi.



# Mahsulotlar bazasi
mahsulotlar = {
    "olma": 10000,
    "banan": 12000,
    "nok": 15000,
    "uzum": 20000
}

savatcha = {}

while True:
    mahsulot = input("Mahsulot nomini kiriting (stop - tugatish): ").lower()
    if mahsulot == "stop":
        break
    if mahsulot in mahsulotlar:
        miqdor = int(input(f"{mahsulot.capitalize()} dan necha dona olasiz? "))
        savatcha[mahsulot] = savatcha.get(mahsulot, 0) + miqdor
    else:
        print("Bunday mahsulot mavjud emas.")

# Jami hisob-kitob
jami = sum(mahsulotlar[m] * savatcha[m] for m in savatcha)

print("\nSiz xarid qilgan mahsulotlar:")
for m, q in savatcha.items():
    print(f"{m.capitalize()} - {q} dona - {q * mahsulotlar[m]} so'm")

print(f"\nJami summa: {jami} so'm")






# 13) So'z teskari yozish dasturi

# Tavsif: Foydalanuvchi so‘z kiritadi, dastur uni teskari ko‘rinishda chiqaradi.



# Lug‘at yordamida so‘zlarni teskari yozish
soz = input("So‘zni kiriting: ").lower()

teskari_soz = "".join(reversed(soz))

print(f"Teskari yozilishi: {teskari_soz}")




# 14) Quiz (Savol-javob o‘yini)

# Tavsif: Foydalanuvchiga savollar berib, javoblarini tekshiruvchi dastur.


# Savollar va javoblar lug'ati
quiz = {
    "O‘zbekiston poytaxti qaysi?" : "toshkent",
    "Python qaysi dasturlash tili?" : "obyektga yo‘naltirilgan",
    "3 + 5 * 2 nechaga teng?" : "13"
}

togri_javoblar = 0

for savol, javob in quiz.items():
    foydalanuvchi_javobi = input(savol + " ").lower()
    if foydalanuvchi_javobi == javob:
        print("To‘g‘ri! ✅")
        togri_javoblar += 1
    else:
        print(f"Xato! To‘g‘ri javob: {javob}")

print(f"\nSiz {len(quiz)} ta savoldan {togri_javoblar} tasiga to‘g‘ri javob berdingiz!")




# 15)  Futbol statistikasi (Jamoalar reytingi)

# Tavsif: Futbol jamoalarining ochkolarini saqlaydi va eng kuchli jamoani chiqaradi.


# Jamoalar ochkolari
jamoalar = {
    "Real Madrid": 85,
    "Barcelona": 82,
    "Manchester City": 90,
    "Bayern Munich": 88
}

# Eng ko'p ochko to'plagan jamoani topish
eng_yaxshi = max(jamoalar, key=jamoalar.get)

print(f"Eng yaxshi jamoa: {eng_yaxshi} ({jamoalar[eng_yaxshi]} ochko)")

