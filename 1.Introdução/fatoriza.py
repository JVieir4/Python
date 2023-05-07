def factoriza(n):
    soma = 0
    for i in range(2,n+1//2):
        if n == 1:
            break
        if n % i == 0:
            soma += i
            while(n%i == 0):
                n /= i
    return soma

def main():
    print("<h3>factoriza</h3>")
    print("in:",6)
    print("out:",factoriza(6))
    
import unittest

class factorizaTest(unittest.TestCase):
    
    def test_factoriza_1(self):
            self.assertEqual(factoriza(28),9)
        
    def test_factoriza_2(self):
            self.assertEqual(factoriza(6),5)
            
if __name__ == '__main__':
    main()
    unittest.main()