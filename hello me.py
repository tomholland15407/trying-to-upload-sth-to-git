name = input("Em be cua ban ten la gi? ")
length = len(name)
if length >= 15:
    gender = "con gai"
elif length <= 15:
    gender = "con trai"
else:
    gender = "con trai"

print(f"\n\nCAM ON BAN DA LAM BAI KHAO SAT, EM BE DANG YEU MANG TEN {name} cua ban co gioi tinh la {gender}!\n")
