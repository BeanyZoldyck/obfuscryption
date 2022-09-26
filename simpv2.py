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
end_key=bytearray(b'*[*[*[')#Literally can be anything (in fact you should decide the best option)
#UzjDYD9rtY
def write(text,path):#use integers instead of bits for some reason... don't see how i missed that..
    with open(path,'rb') as f:
        file = bytearray(f.read())[::-1]
        f.close()
    ext = path.split('.')[-1]
    messBin = bytearray([ord(i) for i in text])
    maxStep = min(int(len(file)/len(text))-2, 255)#foolproof
    lastIndex = 0
    for i,byte in enumerate(messBin):
        file[lastIndex] = byte
        step = randint(2,maxStep)
        file[lastIndex+1] = step
        if i == len(messBin)-1:
            file[lastIndex+1:lastIndex+7] = end_key
            print(file[lastIndex+1:lastIndex+7])
        else:
            lastIndex+=step
    new_path='\\'.join(path.split('\\')[:-1])+f'\\{str(time())[:10]}.{ext}'
    with open(new_path,'wb') as f:
        f.write(file[::-1])
        f.close()
    return new_path
def read(path):
    with open(path,'rb') as f:
        file = bytearray(f.read())[::-1]
        f.close()
    message = bytearray()
    lastIndex = 0
    for index, byte in enumerate(file):
        if index == lastIndex:
            message.append(byte)
            lastIndex+=file[index+1]
            if file[lastIndex+1:lastIndex+7] == end_key:
                return message.decode()+chr(file[lastIndex])
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
