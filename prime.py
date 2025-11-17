l = list(map(int,input().split()))
sum = 0
count = 0
def prime(n):
    if n == 1:
        return 0
    else:

        while True:
            for i in range(2, n):
                if n % i == 0:
                    return 0

            break
        return n
for i in l:
    t = prime(i)
    if t > 1:
        sum += t
        count += 1
print(sum/count)





