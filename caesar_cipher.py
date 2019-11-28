def encrypt(text, s):
    result = ""
    for i in range(len(text)):   #traverse plain text
        char = text[i]
        if (char.isupper()):     # Encrypt uppercase characters in plain text
                result += chr((ord(char) + s - 65) % 26 +65)
        else:                    # Encrypt lowercase characters in plain text
                 result += chr((ord(char) + s - 97) % 26 + 97)
    return result
def decrypt(text, s):
    result1 = ""
    for i in range(len(text)):    # transverse the plain text
        char = text[i]
        if (char.isupper()):       # Encrypt uppercase characters in plain text
                result1 += chr((ord(char) + (28-s) - 65) % 26 +65)
        else:                      # Encrypt lowercase characters in plain text
                 result1 += chr((ord(char) + (28-s) - 97) % 26 + 97)
    return result1

text = input("enter the text to be encrypted:")#eg hell
s = int(input("enter the key :"))#1
encrypt(text, s)
print("Plain Text : " + text)
print("Shift pattern : " + str(s))
print("Encrypted Cipher: " + encrypt(text, s))

decrypt(text,s)
print("decrypted cipher: " + decrypt(text, s))
print("BrutForce Attack.......")
#brutforce attacck
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for key in range(len(LETTERS)):
   translated = ''
   for symbol in text:
      if symbol in LETTERS:
         num = LETTERS.find(symbol)
         num = num - key
         if num < 0:
            num = num + len(LETTERS)
         translated = translated + LETTERS[num]
      else:
         translated = translated + symbol
print('Hacking key is: #%s: %s' % (key, translated))


