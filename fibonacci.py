def fibo(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
# n = int(input('enter number: '))
# print(fibo(n))
import unittest
class Testfibo(unittest.TestCase):
    def test_fibo(self):
        self.assertEqual(fibo(3), 2)
        self.assertEqual(fibo(2), 1)
if __name__ == '__main__':
    unittest.main()