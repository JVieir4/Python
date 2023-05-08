'''
Optimize a seguinte função.
'''
""" 
def duplica(lista):
    if len(lista) == 0:
        return 0
    if len(lista) == 1:
        return 2*lista[0]
    a = lista[0] + duplica(lista[1:])
    b = 2*lista[0] + lista[1] + duplica(lista[2:])
    return max(a,b) """

def duplica(lista):
    n = len(lista)
    if n == 0:
        return 0
    if n == 1:
        return 2 * lista[0]
    res = [0] * n
    res[0] = 2 * lista[0]
    res[1] = max(2 * lista[0] + lista[1], 2 * lista[1] + lista[0])
    for i in range(2, n):
        res[i] = max(res[i-1] + lista[i], res[i-2] + lista[i-1] + 2 * lista[i])
    return res[-1]
    

def main():
    print("<h3>duplica</h3>")
    lista = [5,3,2,4]
    print("in:",lista)
    print("out:",duplica(lista))
    
import unittest

class duplicaTest(unittest.TestCase):

    def test0(self):
            lista = list(range(100))
            self.assertEqual(duplica(lista), 7450)

    def test1(self):
            lista = [5,1,3,4,5,3,1,3,3,5,5,1,2,3,4,5,1,3,4,5,3,1,3,3,5,5,1,2,3,4]
            self.assertEqual(duplica(lista), 149)


if __name__ == '__main__':
    main()
    unittest.main()