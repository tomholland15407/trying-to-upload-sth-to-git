t = 0
r = True
k = 0
def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)
while r:
    if k >= 0:
        a = fact(4*k)
        b = fact(k)
        c = (a*(1103+26390*k))/(b*396**(4*k))
        if c<=10**(-15):
            t += c
            r = False
        else:
            t += c
            k = k+1
print(1/(t*(2**(3/2)/9801)))


