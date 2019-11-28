from crypto import DES
key="hello123"
def pad(text):
    while(len(text)%8!=0):
        text+=' '
    return text
des=DES.new(key,DES.MODE_ECB)
text1="hello hfhdgfhgdfjgfggf"
padded_text=pad(text1)
encrypted_text=des.encrypt(padded_text)
print(encrypted_text)