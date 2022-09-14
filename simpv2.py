from time import time
import colorama
from random import randint
colorama.init(convert=True)
RED = colorama.Style.BRIGHT + colorama.Fore.RED
RESET = colorama.Fore.RESET
GREEN = colorama.Style.BRIGHT + colorama.Fore.GREEN
D_GREEN = colorama.Style.DIM + colorama.Fore.GREEN
BLUE = colorama.Style.BRIGHT + colorama.Fore.CYAN
MAG = colorama.Style.BRIGHT + colorama.Fore.MAGENTA
end_key='*[*[*['#Literally can be anything (in fact you should decide the best option)
keyy_enc=''
#UzjDYD9rtY
for i in end_key:
    keyy_enc+=bin(ord(i))
def normalize(array):
    '''
    Turns dumbass pythoon bytes (0x1101) into normal bytes (0x00001101)
    '''
    if type(array) == list:
        for i in enumerate(array):
            for j in range(8-len(i[1])):
                array[i[0]] = '0' + array[i[0]]
    else:
        for j in range(8-len(array)):
                array = '0' + array
    return array
key_enc = normalize(keyy_enc.split('0b')[1:]) #one line this
def check(path):
    '''
    Just some function I whipped up to test
    '''
    it=0
    g=''
    file = bytearray(open(path,'rb').read())
    for i in file:
        print(normalize(bin(i).replace('0b',''))[-1],end='')
        g+=normalize(bin(i).replace('0b',''))[-1]
        it+=1
        if it % 8 == 0:
            input()
def write(text,path):#use integers instead of bits for some reason... don't see how i missed that..
    with open(path,'rb') as f:
        file = bytearray(f.read())[::-1]
        f.close()
    messBin = bytearray([bin(ord(i)) for i in text])
    maxStep = int(len(file)/len(text))
    
    for i in file
    input(messBin)
    return new_path
def read(path):
    with open(path,'rb') as f:
        file = bytearray(f.read())[::-1]
        f.close()
    message=''
    text_list=[]
    text=''
    for i in file:
        message+=bin(i)[-1]
        try:
            if message[-len(end_key)*8:] == '0010101001011011'*3:#end key in binary
                message = message[:-len(end_key)*8]
                break
        except IndexError:
            pass
    if len(message) % 8 != 0:
        return False
    else:
        for i in range(len(message)):
            if i%8 == 0:
                text_list.append(message[i:i+8])
        for i in text_list:
            text+=chr(int(i,2))
    return text
while True:
    print(BLUE+"\nWelcome to the S.I.M.P (Steganography Interface for Message Privitation)\nPath (q to quit): "+RESET,end='')
    g=input().replace('"','').replace("'","")
    if '\\' in g or ('/' in g):
        print(BLUE+'Read or Write (r/w): '+RESET,end='')
        u = input()
        if u == 'r':
            r = read(g)
            if r:
                print(D_GREEN+'Text: '+RESET+r)
            else:
                print(RED+'\n[Error] Failed to read file'+RESET)
        elif u == 'w':
            print(GREEN+'Message: '+RESET,end='')
            txt=input()
            writh=write(txt,g)
            print(MAG+"\nSuccessfully wrote message! Saved as '"+writh+"'"+RESET)
        else:
            print(RED+"Retard."+RESET)
            input()
    elif g == 'q':
        exit()
