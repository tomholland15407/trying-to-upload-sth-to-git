# # # #memoization fibo
# # # def fib_fast(n, d):
# # #     if n in d:
# # #         return d[n]
# # #     else:
# # #         ans = fib_fast(n-1, d) + fib_fast(n-2, d)
# # #         d[n] = ans
# # #         print(n, ans)
# # #     return ans
# # # d = {1:1, 2:2}
# # # print(fib_fast(4, d))
# #
# # def factorial(n, memo={}):
# #     if n in memo:
# #         return memo[n]
# #     if n == 0 or n == 1:
# #         memo[n] = 1
# #     else:
# #         memo[n] = n * factorial(n-1, memo)
# #     return memo[n]
# # print(factorial(5))  # 120
#
# def hanoi(n,a,b,c):
#     if n == 1:
#         print(f'move 1 from {a} to {b}')
#     else:
#         hanoi(n - 1, a, c, b)
#         print(f'move {n} from {a} to {b}')
#         hanoi(n - 1, c, b, a)
# n = int(input('enter the number of discs: '))
# hanoi(n, 'a', 'b', 'c')