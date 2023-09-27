def repeteee(palavra,n):
    res = ''
    i = 0
    res += palavra
    while palavra[i] == palavra[-(i+1)]:
        i += 1
    res += palavra[i:]*(n-1)
    return res


def main():
    print("<h3>repete</h3>")
    print("in:","amanha",2)
    print("out:",repeteee("amanha",2))
    
import unittest

class repeteTest(unittest.TestCase):
    
    def test_repete_1(self):
            self.assertEqual(repeteee("amanha",2),"amanhamanha")

    def test_repete_2(self):
            self.assertEqual(repeteee("ola",3),"olaolaola")
            
if __name__ == '__main__':
    main()
    unittest.main()