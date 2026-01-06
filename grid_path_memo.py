m = int(input())
n = int(input())

def pathways(m,n, memo={}):
    if (m,n) in memo:
        return memo[(m,n)]
    if m == 0  or n == 0:
        memo[(m,n)] = 1
    else:
        memo[(m,n)] = pathways(m-1, n, memo) + pathways(m, n-1, memo)
    return memo[(m,n)]
print(pathways(m,n))




#
#     if m == 0 or n == 0:
#         return 1
#     else:
#         return pathways(m-1,n) + pathways(m,n-1)
# print(pathways(m,n))
#
