from os import walk, path
from getpass import getuser
y = 1
#this file is fucking awfu - note from 2022/9/14
if y == 0:
    direct = f'C:\\Users\\{getuser()}\\Videos\\temp\\pre'
else:
    direct = f'C:\\Users\\{getuser()}\\Videos\\temp\\Captures'
def get_files(direct):
    fies = []
    for i,_,j in walk(direct):
        for k in j:
            fies.append(path.join(i,k))
    return fies
files=get_files(direct)
def encr(files):
    temp = open(files,'rb').read()[::-1]
    try:
        open(files,'wb').write(temp)
    except PermissionError:
        pass
    temp=''
#encr("C:\\Users\\chuka\\Downloads\\literallythesameimage - Copy.png")
for i in files:
    encr(i)
