# 1. Roʻyxatdagi eng katta va eng kichik sonni topish


sonlar = [5, 2, 9, 1, 5, 6]

eng_katta = max(sonlar)
eng_kichik = min(sonlar)

print(f"Eng katta son: {eng_katta}")
print(f"Eng kichik son: {eng_kichik}")


# 2. Roʻyxatdagi sonlarning yigʻindisini hisoblash


sonlar = [1, 2, 3, 4, 5]

yigindi = sum(sonlar)
print(f"Sonlar yigʻindisi: {yigindi}")


# 3. Roʻyxatdagi juft sonlarni topish


sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

juft_sonlar = [son for son in sonlar if son % 2 == 0]
print(f"Juft sonlar: {juft_sonlar}")


# 4. Roʻyxatdagi elementlarni teskari tartibda chiqarish


mevalar = ["olma", "banan", "anor", "uzum"]

teskari = mevalar[::-1]
print(f"Teskari tartib: {teskari}")


# 5. Roʻyxatdagi elementlarni sanash


mevalar = ["olma", "banan", "olma", "uzum", "banan", "olma"]

sanash = {}
for meva in mevalar:
    if meva in sanash:
        sanash[meva] += 1
    else:
        sanash[meva] = 1

print(f"Elementlar soni: {sanash}")


# 6. Roʻyxatdagi elementlarni almashtirish


mevalar = ["olma", "banan", "anor", "uzum"]


index = mevalar.index("banan")
mevalar[index] = "shaftoli"

print(f"Yangilangan roʻyxat: {mevalar}")

# 7. Roʻyxatdagi elementlarni saralash


mevalar = ["olma", "banan", "anor", "uzum"]

mevalar.sort()
print(f"Saralangan roʻyxat: {mevalar}")


# 8. Roʻyxatdagi elementlarni qidirish


mevalar = ["olma", "banan", "anor", "uzum"]

qidiruv = "banan"
if qidiruv in mevalar:
    print(f"{qidiruv} roʻyxatda mavjud")
else:
    print(f"{qidiruv} roʻyxatda mavjud emas")


# 9. Roʻyxatdagi elementlarni birlashtirish 


mevalar1 = ["olma", "banan"]
mevalar2 = ["anor", "uzum"]

birlashgan = mevalar1 + mevalar2
print(f"Birlashgan roʻyxat: {birlashgan}")




