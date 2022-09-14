from secrets import choice
from string import ascii_letters, digits, punctuation
from pyperclip import copy
from functools import reduce

def encrypt(text):
    possible = ascii_letters+digits*3
    cryptDictionary = {}
    for i in range(1,96):
        exec(f'c{i} = "'+choice(possible)+choice(possible)+choice(possible)+'"', cryptDictionary)
    del cryptDictionary['__builtins__']
    crypts=list(cryptDictionary.values())
    hashList = [reduce(lambda x,y: ord(x)*ord(y) if type(x) == str else x*ord(y), i) for i in crypts]
    theresDuplicates = len(hashList) != len(set(hashList))
    while theresDuplicates:
        for i in enumerate(hashList):
            if hashList.count(i[1]) > 1:
                exec('c'+str(i[0]+1)+' = "'+choice(possible)+choice(possible)+choice(possible)+'"',cryptDictionary)
                exec(f'hashList[{i[0]}] = reduce(lambda x,y: ord(x)*ord(y) if type(x) == str else x*ord(y), "{cryptDictionary["c"+str(i[0]+1)]}")', {'hashList':hashList, 'reduce':reduce})
        theresDuplicates = len(hashList) != len(set(hashList))
        if not theresDuplicates:
            del cryptDictionary['__builtins__']
            break
    possibleInputs = ascii_letters+' '+digits+punctuation
    a_to_x_dict = {i:j for i,j in zip(possibleInputs, cryptDictionary.values())}
    prime_numbers = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293)
    decode_library = {i:j for i,j in zip(ascii_letters+digits,prime_numbers)}
    keyDictionary = {}
    for i in range(1,96):
        exec(f's{i} = 1', keyDictionary)
    for i in enumerate(cryptDictionary.values()):
        keyDictionary[f's{i[0]+1}'] = reduce(lambda x,y: decode_library[x]*decode_library[y] if type(x) == str else x*decode_library[y],i[1])
    del keyDictionary['__builtins__']
    text_encoded = ""
    key = ''.join([str(i)+choice(ascii_letters) for i in list(keyDictionary.values())])
    try:
        for i in text:
            text_encoded += a_to_x_dict[i]
        return text_encoded+ key + str(3*len(text))
    except KeyError:
        input("Unrecognized character used. Press Enter to exit\n")
        return False
if __name__ == '__main__':
    copy(encrypt(input("Text to encrypt\n")))
    input("Encrypted text has been copied to the clipboard\n")
