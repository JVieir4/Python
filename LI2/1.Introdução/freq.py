
def frequencia(texto):
    la2 = {}
    for p in texto.split():
        if p not in la2:
            la2[p] = 1
        else:
            la2[p] += 1

    abcsort =(list(la2.keys()))
    abcsort.sort()
    ans = (sorted(abcsort, key = lambda p:la2[p], reverse= True))
    return ans

def main():
    print("<h3>frequencia</h3>")
    texto = "o tempo perguntou ao tempo quanto tempo o tempo tem"
    print("in:",texto)
    print("out:",frequencia(texto)) 
    
import unittest

class frequenciaTest(unittest.TestCase):
    
    def test_frequencia_1(self):
        self.assertEqual(frequencia("o tempo perguntou ao tempo quanto tempo o tempo tem"),['tempo','o','ao','perguntou','quanto','tem'])

    def test_frequencia_2(self):
        self.assertEqual(frequencia("ola"),['ola'])
            
if __name__ == '__main__':
    main()
    unittest.main()