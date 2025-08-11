character_name = input("Ten cua ban la gi? ")
if character_name == "Hung":
    age = 18
    food = "chuoi"
    quality = "thong minh"
elif character_name == "Ngoc Anh":
    age = 11
    food = "bim bim"
    quality = "rat ngo"
else:
    age = "chua ro"
    food = "chua ro"
    quality = "chua ro"
print(f"\nCam on {character_name} vi da thuc hien bai test nay.")
print(f"\nTuoi cua ban la {age} va mon an ban thich la {food}.")
print(f"\nSau rat nhieu nghien cuu, chung toi da tim ra ban la mot nguoi {quality}.")
print(f"\nCam on ban {character_name} mot lan nua .")
print(f"Tat ca nhung gi o tren la su that.\n")

