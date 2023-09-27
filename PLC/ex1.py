import re

line1 = "hello world"
line2 = "goodbye world"
line3 = "hi, hello there"

#1.1
print('\n1.1_____________________')
if re.match(r'hello',line3):
    print('match')
else:
    print('no hello found (no inicio da string)')
  
# 1.2
print('\n1.2_____________________')
if re.search(r'hello', line1):
    print('<<hello>> foi encontrado na string')
else:
    print('Não foram encontradas nenhumas ocorrências da palavra <<hello>>')

# 1.3
print('\n1.3_____________________')  
line = "Hello there! Uh, hi, hello, it's me... Heyyy, hello? HELLO!"
linee = "Hello hEllo heLlo hellO HellO hELLo"
print(re.findall(r'[Hh]ello', line))
#print(re.findall(r'[Hh][eE][lL]+[oO]', linee)) fica ['Hello', 'hEllo', 'heLlo', 'hellO', 'HellO', 'hELLo']

# 1.4
print('\n1.4_____________________')
line = "Hello there! Uh, hi, hello, it's me... Heyyy, hello? HELLO!"
if res := re.sub(r'(?i:hello)', '*YEP*', line, count = 0):
    print(res)

# 1.5
print('\n1.5_____________________')
line = "bananas, laranjas, maçãs, uvas, melancias, cerejas, kiwis, etc."
if res := re.split(', ', line, maxsplit = 0):
    print(res)
    
# 2
print("\n2_______________________")
def palavra_magica(frase):
  if re.search(r'por[ \t]+favor[.?!;]$', frase):
      return "True"

print(palavra_magica("Posso ir à casa de banho, por  favor?"))
print(palavra_magica("Preciso de um favor."))

# 3
print("\n3_______________________")
def narcissismo(linha):
  if res := re.findall('(?i:eu)',linha):
      #^(?i:eu)[ \t,.!?\n]+|[^a-zA-Z]+(?i:eu)[ \t,.!?\n]+
      return len(res)

print(narcissismo("Eu não sei se eu quero continuar a ser eu. romeu auea Por outro lado, eu ser eu é uma parte importante de quem EU sou."))

# 4
print("\n4_______________________")
def troca_de_curso(line1, novo_curso):
  if res := re.sub("LEI", novo_curso, line1, count = 0):
    print(res)

#print(troca_de_curso("LEI é o melhor curso! Adoro LEI! Gostar de LEI devia ser uma lei.", input("Novo curso? ")))

# 5
print("\n5_______________________")
def soma_string(linha):
  if res := re.split(',',linha):
      return sum([int (i) for i in res])

print(soma_string("4,10,-6,2,3,8,-3,0,2,-5,1"))

# 6
print("\n6_______________________")
def pronomes(frase):
  if res := re.findall('(?i:eu)|(?i:tu)|(?i:el[ea]s?)|(?i:nós)|(?i:vós)', frase):
      return res
      
print(pronomes("eu me tu you ele him ela her eles them elas elasss nós we vós avós olá amigos"))

# 7
print("\n7_______________________")
def variavel_valida(id):
  return bool(re.match('^[A-Za-z][A-Za-z0-9_]*', id))

print(variavel_valida("0qwerty_03"))

# 8
print("\n8_______________________")
def inteiros(frase):
    if res := re.findall('-?\d+',frase):
        return res
print(inteiros("eu tinha 10 bolos, fiquei com -6 quando o meu irmão tirou 2 e o meu pai 4."))

def underscores( frase ):
  
  return frase

# 8
print("\n8_______________________")
print(underscores("Aqui temos   um belo   exemplo   de frase    completamente  maluca  !"))