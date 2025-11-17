password = input("Enter a password: ")

if len(password) < 8:
    print("Too short")
else:
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in '!@#$%^&*' for c in password)
    if has_upper and has_lower and has_digit and has_special:
        print("Yes")
    else:
        if not has_upper:
            print('upper')
        if not has_lower:
            print('lower')
        if not has_digit:
            print('digit')
        if not has_special:
            print('special')