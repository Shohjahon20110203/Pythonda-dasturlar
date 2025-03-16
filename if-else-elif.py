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
