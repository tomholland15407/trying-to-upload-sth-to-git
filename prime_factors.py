def prime(n):
    if n == 1:
        return False
    else:
        r = True
        while r:
            for i in range(2, n):
                if n % i == 0:
                    return False

            break
        return True

def factors(n):
    factors = {}
    power = 0
    for i in range(2, n):
        if prime(i) == True and n % i == 0:
            for k in range(1,n):
                if n % (i**k) == 0:
                    power += 1
            factors[i] = power
            power = 0
    return factors
dict_1 = factors(50)
def prime_format(fact_dict):
    return ' * '.join(f'{prime}^{power}' for prime, power in fact_dict.items())
print(prime_format(dict_1))
dict_2 = factors(75)
print(prime_format(dict_2))

gcd = {}
for i in dict_1:
    if i in dict_2:
        gcd[i] = min(dict_1[i], dict_2[i])
a = 1
for p in gcd:
    a *= p**gcd[p]
print(a)

for i in dict_2:
    if i in dict_1:
        dict_1[i] = max(dict_1[i], dict_2[i])
    else:
        dict_1[i] = dict_2[i]

t = 1
for i in dict_1:
    t *= i**dict_1[i]
print(t)

gcd_dict = {}
for p in dict_1:
    if p in dict_2:
        gcd_dict[p] = min(dict_1[p], dict_2[p])


