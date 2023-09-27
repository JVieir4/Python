'''
Implemente uma função que determine em quantas sequências de n bits
um bit a 1 apenas aparece em sequências de pelo menos k 1s seguidos. 
Por exemplo se n = 3 e k = 2 então temos 4 sequências válidas, 
nomeadamente 000, 110, 011 e 111. Se n = 4 e k = 3 temos também 4 
sequências válidas, nomeadamente 0000, 1110, 0111 e 1111. Se n = 4 e 
k = 2 então já temos 7 sequências válidas: para além das 4 anteriores 
temos 1100, 0110 e 0011.
'''

def aux(n):
    combinations = []

    def combs(p, r):
        if r == 0:
            combinations.append(p)
        else:
            combs(p + '0', r - 1)
            combs(p + '1', r - 1)

    combs('', n)
    return combinations
    
def bits(n, k):
    if k > n:
        return 0
    total = 0
    for x in aux(n):
        uns = x.count('1')
        if '1' * k in x:
            if uns >= k and '1' * uns in x:
                total+=1
    return total+1


def main():
    print("<h3>bits</h3>")
    n = 4
    k = 2
    print("in:",n,k)
    print("out:",bits(n,k))

import unittest

class bitsTest(unittest.TestCase):

    def test_0(self):
            n = 8
            k = 2
            self.assertEqual(bits(n,k),65)

    def test_1(self):
            n = 5
            k = 3
            self.assertEqual(bits(n,k),7)

            
if __name__ == '__main__':
    main()
    unittest.main()
