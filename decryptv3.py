from string import ascii_letters, digits, punctuation
from functools import reduce
import colorama
colorama.init(convert=True)
RESET = colorama.Fore.RESET
RED = colorama.Style.BRIGHT + colorama.Fore.RED
def decrypt(operation):
    hashIt = lambda x,y: ord(x)*ord(y) if type(x) == str else x*ord(y)
    prime_numbers = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293)
    decode_library = {i:j for i,j in zip(prime_numbers,ascii_letters+digits)}
    possibles = ascii_letters+' '+digits+punctuation
    for i in enumerate(operation[::-1]):
        if i[1] in ascii_letters:
            try:
                length = int(operation[-i[0]:])
            except IndexError:
                input("Decode Error: undetecable text inputted. Press Enter to exit\n")
                return False
            operation = operation[:-i[0]-1]
            break
    input = operation[:length]
    keys = operation[length:]
    key=''
    real_list = []
    for i in keys:
        if i in ascii_letters:
            key += ':'
        else:
            key += i
    for i in key.split(":"):
        real_list.append(int(i))
    pri_li1 = []
    pri_li = []
    for i in real_list:
        for j in prime_numbers:
            if i % j == 0:
                pri_li1.append(j)
                if i % (j**2) == 0:
                    pri_li1.append(j)
                    if i % (j**3) == 0:
                        pri_li1.append(j)
        pri_li.append(pri_li1)
        pri_li1 = []
    final_dict = {reduce(hashIt, [decode_library[j] for j in i]):j for i,j in zip(pri_li,possibles)}
    inp_list = [input[i:i+3] for i in range(0,len(input),3)]
    message = ''
    for i in inp_list:
        message += final_dict[reduce(hashIt, i)]
    return message
if __name__ == '__main__':
    input(decrypt(input("Output:\n")))
