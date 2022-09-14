from string import ascii_letters
def decrypt(operation):
    decode_library = {
    2: 'a',
    3: 'b',
    17: 'c',
    53: 'd',
    59: 'e',
    61: 'f',
    67: 'g',
    71: 'h',
    73: 'i',
    79: 'j',
    83: 'k',
    89: 'l',
    97: 'm',
    101: 'n',
    103: 'o',
    107: 'p',
    109: 'q',
    113: 'r',
    127: 's',
    131: 't',
    137: 'u',
    139: 'v',
    149: 'w',
    151: 'x',
    157: 'y',
    163: 'z',
    167: 'A',
    173: 'B',
    179: 'C',
    181: 'D',
    191: 'E',
    193: 'F',
    197: 'G',
    199: 'H',
    211: 'I',
    223: 'J',
    227: 'K',
    229: 'L',
    233: 'M',
    239: 'N',
    241: 'O',
    251: 'P',
    257: 'Q',
    263: 'R',
    269: 'S',
    271: 'T',
    277: 'U',
    281: 'V',
    283: 'W',
    293: 'X',
    307: 'Y',
    311: 'Z',
    313: '0',
    317: '1',
    331: '2',
    337: '3',
    347: '4',
    349: '5',
    353: '6',
    359: '7',
    367: '8',
    373: '9'
}
    possibles = (
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'," ",'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',"1","2","3","4","5","6","7","8","9","0",'"',"'",",",":",";","(",")","[","]","~","-","_","+","=","/",".","?","\\",'`',">","<","|","{","}","+","=","*","&","^","%","$","#","@","!",)
    prime_numbers = (
    2, 3, 17, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151,
    157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373)
    for i in enumerate(list(operation)):
        if i[1] in ascii_letters:
            
    inp = #operation.split(',')[0]
    
    try:
        key1 = operation.split(',')[1]
    except IndexError:
        input("Decode Error: undetecable text inputted. Press Enter to exit\n")
        quit()
    key2 = list(key1)
    it = 0
    real_list = []
    for i in enumerate(key2):
        if i[1] in ascii_letters:
            key2[i[0]] = ':'
    key = str(key2).replace(",",'').replace("'",'').replace(" ",'').replace('"','').replace("[",'').replace("]",'')
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
    r = []
    for j in pri_li:
        try:
            r.append((decode_library[j[0]]+decode_library[j[1]]+decode_library[j[2]],possibles[it]))
            it += 1
        except IndexError:
            pass
    final_dict = dict(r)
    inp_list = []
    final_list=[]
    tits=[]
    for i in enumerate(inp):
        if (i[0]+1) % 3 == 0 and i[0] != 0:
            inp_list.append(inp[i[0]-2]+inp[i[0]-1]+i[1])
    for i in inp_list:
        for a in i:
            for b in i:
                for c in i:
                    gee = a + b + c
                    if gee.count(a) > i.count(a):
                        pass
                    elif gee.count(b) > i.count(b):
                        pass
                    elif gee.count(c) > i.count(c):
                        pass
                    else:
                        try:
                            p = final_dict[gee]
                            final_list.append(p)
                            break
                        except KeyError:
                            pass
    for i in inp_list:
        tits.append(inp_list.count(i))
    for i in enumerate(final_list):
        if final_list.count(i[1]) != tits[i[0]]:
            for u in range(final_list.count(i[1]) - tits[i[0]]):
                del final_list[i[0]]
    return ''.join(final_list)
if __name__ == '__main__':
    print(decrypt(input("Output:\n")))
    input()
