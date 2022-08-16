

import numpy as np
import json
import os
np_file_path = "./resource/templates/interface_object.npy"
path = './templates/'
dir_list = os.listdir(path)

print(dir_list)
data_dic = {}
for i in dir_list:
    data = open(f"{path}/{i}").read()
    data_dic[f"{i}"] = data
print(type(json.dumps(data_dic).encode()))

#data = json.loads(str(np.load(np_file_path)))


from cryptography.fernet import Fernet
# key generation
key = Fernet.generate_key()
  
# string the key in a file
with open('filekey.key', 'wb') as filekey:
   filekey.write(key)

print("Key : ", key.decode())
f = Fernet(b'1CGEV8wgZf65YNul-rxyQlemoeObkyW1-TmBfZEQFZo=')
encrypted_data = f.encrypt(json.dumps(data_dic).encode())
#print("After encryption : ", encrypted_data)
with open('encryption.txt', 'wb') as filekey:
   filekey.write(encrypted_data)
np.save(np_file_path, encrypted_data)


#decrypted_data = np.load(np_file_path) 
#data = json.loads(f.decrypt(decrypted_data.tobytes()).decode())
#print(data['index.html'])
from main import *
run_sys()

