from string import ascii_letters
def decrypt(operation):
    decode_library = {
    2:'a',
    3:'b',
    5:'c',
    7:'d',
    11:'e',
    13:'f',
    17:'g',
    19:'h',
    23:'i',
    29:'j',
    31:'k',
    37:'l',
    41:'m',
    43:'n',
    47:'o',
    53:'p',
    59:'q',
    61:'r',
    67:'s',
    71:'t',
    73:'u',
    79:'v',
    83:'w',
    89:'x',
    97:'y',
    101:'z',
    107:'A',
    109:'B',
    113:'C',
    127:'D',
    131:'E',
    137:'F',
    139:'G',
    149:'H',
    151:'I',
    157:'J',
    163:'K',
    167:'L',
    173:'M',
    179:'N',
    181:'O',
    191:'P',
    193:'Q',
    197:'R',
    199:'S',
    211:'T',
    223:'U',
    227:'V',
    229:'W',
    233:'X',
    239:'Y',
    241:'Z',
    251:"1",
    257:"2",
    263:"3",
    269:"4",
    271:"5",
    277:"6",
    281:"7",
    283:"8",
    293:"9",
    307:"0"
    }
    possibles = (
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'," ",'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',"1","2","3","4","5","6","7","8","9","0",'"',"'",",",":",";","(",")","[","]","~","-","_","+","=","/",".","?","\\",'`',">","<","|","{","}","+","=","*","&","^","%","$","#","@","!",)
    prime_numbers = (
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157,
    163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307)
    inp = operation.split(',')[0]
    try:
        key2 = list(operation.split(',')[1])
    except IndexError:
        input("Decode Error: undetecable text inputted. Press Enter to exit\n")
        quit()
    it = 0
    real_list = []
    for i in enumerate(key2):
        if i[1] in ascii_letters:
            key2[i[0]] = ':'
    key = ''.join(key2)
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
    for i in decrypt(input("Output:\n")):
        print(i,end='')
    input()
