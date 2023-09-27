"""
Na cifra de Vigenère, dado um texto e uma chave (esta só com letras minúsculas), 
cada letra do texto é cifrada aplicando um desvio correspondente à posição no 
alfabeto da letra respetiva na chave. 
Por exemplo, para cifrar "BoaTarde" com a chave "ola", temos que repetidamente 
aplicar os desvios 14, 11, e 0. Como 'B'+14 == 'P', 'o'+11 == 'z', 'a'+0 == 'a',
'T'+14 == 'H', 'a'+11 == 'l', 'r'+0 = 'r', 'd'+14=='r', e 'e'+11 == 'p', o 
criptograma resultante seria "PzaHlrrp".
Implemente a função que decifra um criptograma cifrado com esta técnica.
"""

def decifrar(texto,chave):
    abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    decifrado = ""
    key = chave
    i = 0
    res = ""
    while len(key) < len(texto):
        key = key+chave
    for l in texto:
        if(l.isupper()):
            l = l.lower()
            dif = ord(l)-ord('a') - (ord(key[i])-ord('a'))
            res = abc[dif].upper()
        else:
            dif = ord(l)-ord('a') - (ord(key[i])-ord('a'))
            res = abc[dif]
        decifrado = decifrado + res
        i+=1
    return decifrado

def main():
    print(ord('A'))
    print(chr(ord('A') - 15))
    print("<h4>decifrar</h4>")
    print(decifrar("AyuvfnimkpcfScTsubggmtwnXG","python"))
    
import unittest

class test(unittest.TestCase):

    def test0(self):
            self.assertEqual(decifrar("AyuvfnimkpcfScTsubggmtwnXG","python"),"LaboratoriosDeAlgoritmiaII")
            

    def test1(self):
            self.assertEqual(decifrar("WkeppetcvftcPoEtgpnkcdFcNqoawvlecz","lcc"),"LicenciaturaEmCienciasDaComputacao")

if __name__ == '__main__':
    main()
    unittest.main()