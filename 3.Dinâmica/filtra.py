'''
Implemente a função filtra por forma a filtrar as strings que concordam com um padrão.
Uma string concorda com um padrão se for possível obtê-la a partir
do padrão substituindo cada caracter '?' por uma letra e cada caracter '*' por um
número arbitrário de letras. Por exemplo, 'aabxaxb' concorda com o padrão 'a*?b',
enquanto que 'ab' já não.
'''


#####################
#        50%        #
#####################

def encontra(padrao):
    i=0
    
    if padrao=="":
      return 0
    
    for letra in padrao:
        if letra != '*':
            return i
        i+=1
            
    return -1
    
def aceite(padrao, palavra):
    if encontra(padrao)==(-1):
        return 1
        
    elif palavra == "":
        if padrao == "":
            return 1
        else:
            return 0
            
    elif padrao == "":
        return 0
       
    else:
        if padrao[0] == '?':
            r = aceite(padrao[1:], palavra[1:])
        elif padrao[0] == '*':
            res = encontra(padrao)
            r = aceite(padrao[1:], palavra[res:])
        else:
            if(padrao[0] == palavra[0]):
                r = aceite(padrao[1:], palavra[1:])
            else:
                return 0

    return r
    
def filtra(padrao, strings):
    r = []
    if strings==[]:
        return []
    for palavra in strings:
        if aceite(padrao, palavra)== 1:
            r.append(palavra)
        
    return r



#####################
# Solução com regex #
#        80%        #
#####################

import re
    
def filtra(padrao, strings):
    regex = ""
    
    for letra in padrao:
        
        if letra == '?':
            regex += "[a-zA-Z ]"
            
        elif letra == '*':
            regex += "[a-zA-Z ]*"
            
        else:
            regex += letra
            
    regex += "$"
            
    r = []
    
    for string in strings:
        
        y = re.match(regex, string)
        
        if y:
            r.append(string)
        
    return r