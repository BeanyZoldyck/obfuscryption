from zipfile import ZipFile, ZIP_DEFLATED
from random import shuffle
from colorama import Fore
from colorama import init
from os import remove, walk
from os import path as p
from time import time
init()
CYAN = Fore.LIGHTCYAN_EX
RESET = Fore.RESET
class Terminate():
    pass
def encrypt_bytes(path,path2=""):
    nfn = path.split('\\')[-1].split('.')[0]
    typ = path.split('\\')[-1].split('.')[1]
    bytes_obj_ue = list(bytearray(open(path,'rb').read()))
    fourth = int(len(bytes_obj_ue)/4)
    try:
        tings = [bytes_obj_ue[i:i+fourth] for i in range(0,len(bytes_obj_ue),fourth)]
    except ValueError:
        pass
    else:
        key_one = ''
        key_two =''
        key_three=''
        key_four=''
        byte_1=[]
        byte_2=[]
        byte_3=[]
        byte_4=[]
        ting1 = list(enumerate(tings[0]))
        ting2 = list(enumerate(tings[1]))
        ting3 = list(enumerate(tings[2]))
        ting4 = list(enumerate(tings[3]))
        shuffle(ting1)
        shuffle(ting2)
        shuffle(ting3)
        shuffle(ting4)
        for j in ting1:
            key_one+=hex(j[0])
            byte_1.append(j[1])
        for j in ting2:
            key_two+=hex(j[0])
            byte_2.append(j[1])
        for j in ting3:
            key_three+=hex(j[0])
            byte_3.append(j[1])
        for j in ting4:
            key_four+=hex(j[0])
            byte_4.append(j[1])    
        open(f'{nfn}.key','w').write(nfn+f'.{typ},'+f'{key_one}:::{key_two}:::{key_three}:::{key_four}')
        open('1.enc','wb').write(bytearray(byte_1))
        open('2.enc','wb').write(bytearray(byte_2))
        open('3.enc','wb').write(bytearray(byte_3))
        open('4.enc','wb').write(bytearray(byte_4))
        zipf = ZipFile(path2+f'{nfn}.zip','w',ZIP_DEFLATED)
        zipf.write(f'{nfn}.key')
        remove(f'{nfn}.key')
        for i in range(1,5):
            zipf.write(str(i)+'.enc')
            remove(str(i)+'.enc')
        zipf.close()
    #print(CYAN + '\n[Notice]: '+RESET+f'File saved as "{nfn}.zip"',end=": ")
def decrypt_bytes(path,path2=""):
    if path[-4:] == '.zip':
        code = path.split('\\')[-1].replace('.zip','')
        zipf = ZipFile(path)
        bytes_obj_e1=bytearray(zipf.open('1.enc').read())
        bytes_obj_e2=bytearray(zipf.open('2.enc').read())
        bytes_obj_e3=bytearray(zipf.open('3.enc').read())
        bytes_obj_e4=bytearray(zipf.open('4.enc').read())
        whole_key_file = str(zipf.open(code+'.key','r').read()).replace('\'','')
        zipf.close()
        bytes_obj_ue1 = []
        bytes_obj_ue2 = []
        bytes_obj_ue3 = []
        bytes_obj_ue4 = []
        length_one = len(bytes_obj_e1)
        length_two = len(bytes_obj_e4)
        for i in range(length_one):
            bytes_obj_ue1.append(b'')
            bytes_obj_ue2.append(b'')
            bytes_obj_ue3.append(b'')
        for i in range(length_two):
            bytes_obj_ue4.append(b'')
        name = whole_key_file.split(',')[0]
        all_indices = whole_key_file.split(',')[1].split(':::')
        key1 = all_indices[0].split('0x')[1:]
        key2 = all_indices[1].split('0x')[1:]
        key3 = all_indices[2].split('0x')[1:]
        key4 = all_indices[3].split('0x')[1:]
        for i in enumerate(key1):
            bytes_obj_ue1[int('0x'+i[1],16)] = bytes_obj_e1[i[0]]
        for i in enumerate(key2):
            bytes_obj_ue2[int('0x'+i[1],16)] = bytes_obj_e2[i[0]]
        for i in enumerate(key3):
            bytes_obj_ue3[int('0x'+i[1],16)] = bytes_obj_e3[i[0]]
        for i in enumerate(key4):
            bytes_obj_ue4[int('0x'+i[1],16)] = bytes_obj_e4[i[0]]
        with open(path2+name[1:],'wb') as f:
            f.write(bytearray(bytes_obj_ue1))
            f.write(bytearray(bytes_obj_ue2))
            f.write(bytearray(bytes_obj_ue3))
            f.write(bytearray(bytes_obj_ue4))
            f.close()
        remove(path)
g = 0
itera = 0
tyme_started=time()
folder_encr = "D:\\belle.delphine"
folder_save = "D:\\qtipmaddieencrpytiontest\\"
Im_lazy='d'
if Im_lazy == 'e':
    for i,_,j in walk(folder_encr):
        g = len(j)
        for k in j:
            itera+=1
            #encrypt_bytes(p.join(i,k),folder_save)
            print(CYAN + '[Progress]: '+RESET+str(itera*100/g)[:4]+'% done',end='\r')
            #input()
elif Im_lazy == 'd':
    for i,_,j in walk(folder_save):
        g = len(j)
        for k in j:
            decrypt_bytes(p.join(i,k),folder_save)
            itera+=1
            print(CYAN + '[Progress]: '+RESET+str(itera*100/g)[:4]+'% done',end='\r')
            #input()
input("Time elapsed: "+str(time()-tyme_started)[:6]+' seconds')
