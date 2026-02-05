def age_check(age):
    if age >= 18:
        return True
    elif age <= 0:
        raise ValueError('age must be greater than 0')
    else:
        return False
print(age_check(18))
print(age_check(10))
print(age_check(-18))