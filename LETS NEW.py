print(f"Lai la Hung day, va hom nay chung minh se co mot tro choi moi")
guess = int(input(f"\nVa tro choi do chinh la doan gio hung thi GPLX vao ngay mai, ban co 7 lan doan, hay chon 1 con so tu 0 den 24.\n"))
secret = 13
guess_count = 1
while guess != secret:
    if guess_count >= 7:
        print('\nDap an chinh xac la 13h chieu mai, see you soon!\n')
        break
    guess = int(input(f'\nDo chua phai la dap an chinh xac, ban con {7 - guess_count} lan doan.\n'))
    guess_count += 1
else: print('\nChinh xac lun, love uuu!\n')
