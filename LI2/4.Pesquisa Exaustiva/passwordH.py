import string

def complete(h,c):                      #The complete function checks if the length of c is equal to 4. If it is, it returns True;
    return len(c) == 4                  #otherwise, it returns False. This function is used to determine if the sequence c is complete.

def extensions(h,c):                    #The extensions function returns all uppercase letters of the alphabet.
    return string.ascii_uppercase       #It utilizes the string.ascii_uppercase constant from the Python string module.

def valid(h,c):                         #The valid function checks if the hash of c is equal to the provided hash value h.If they match, it
    return h == hash(c)                 #returns True; otherwise, it returns False. This function is used to validate if c is a valid solution.

def search(h):                          #The search function initializes an empty list c and attempts to find a valid sequence by calling the
    c = []                              #aux function with the provided hash value h and the empty list c. If aux returns True, indicating that
    if aux(h,c):                        #a valid sequence was found, the function returns the sequence c. Otherwise, it returns None.
        return c

def aux(h,c):                           #The aux function is the core recursive function that performs the search. It takes the hash value h and
    if complete(h,c):                   #the list c as arguments. It checks if c is complete using the complete function. If c is complete, it
        return valid(h,c)               #checks if it is a valid solution using the valid function and returns the result.
    for x in extensions(h,c):           #If c is not complete, the function iterates over each character x from the extensions obtained from the
        c.append(x)                     #extensions function. It appends x to c, and then recursively calls aux with the updated h and c. If the
        if aux(h,c):                    #recursive call returns True, indicating a valid solution was found, the function immediately returns
            return True                 #True to propagate the result up the call stack.
        c.pop()                         #If the recursive call does not return True, the function removes the last character from c using c.pop()
    return False                        #to backtrack and continue the search with the next extension.