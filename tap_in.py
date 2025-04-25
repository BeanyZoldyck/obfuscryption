from encode import encode, decode
from os import walk, path

directory = input("Dir: ").replace('"','')
password = input("Password (default is test): ")
code = input("Encode or Decode (default is d): ")
task = (decode,encode)[code == 'e']
for i,_,j in walk(directory):
    for k in j:
        task(path.join(i,k), password)
input('finished')
