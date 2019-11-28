def caesarEncrypt(plaintext, shift):
    return caesarCipher(True, plaintext, shift)


def caesarDecrypt(ciphertext, shift):
    return caesarCipher(False, ciphertext, shift)


def caesarCipher(encrypt, text, shift):
    if not shift in range(0, 25):
        raise Exception('Key value out of range')

    output = ""
    for c in text:
        # only encrypt alphanumerical characters
        if c.isalpha():
            # we want to shift both upper- and lowercase characters
            ci = ord('A') if c.isupper() else ord('a')

            # if not encrypting, we're decrypting
            if encrypt:
                output += caesarEncryptCharacter(c, ci, shift)
            else:
                output += caesarDecryptCharacter(c, ci, shift)
        else:
            # leave other characters such as digits and spaces
            output += c
    return output


def caesarEncryptCharacter(plaintextCharacter, positionOfAlphabet, shift):
    # convert character to the (zero-based) index in the alphabet
    n = ord(plaintextCharacter) - positionOfAlphabet
    # perform the >positive< modular shift operation on the index
    # this always returns a value within the range [0, 25]
    # (note that 26 is the size of the western alphabet)
    x = (n + shift) % 26  # <- the magic happens here
    # convert the index back into a character
    ctc = chr(x + positionOfAlphabet)
    # return the result
    return ctc


def caesarDecryptCharacter(plaintextCharacter, positionOfAlphabet, shift):
    # convert character to the (zero-based) index in the alphabet
    n = ord(plaintextCharacter) - positionOfAlphabet
    # perform the >negative< modular shift operation on the index
    x = (n - shift) % 26
    # convert the index back into a character
    ctc = chr(x + positionOfAlphabet)
    # return the result
    return ctc


def encryptDecrypt():
    print('--- Run normal encryption / decryption')
    plaintext = 'Hello world!'
    key = 3  # the original value for the Caesar cipher
    ciphertext = caesarEncrypt(plaintext, key)
    print(ciphertext)
    decryptedPlaintext = caesarDecrypt(ciphertext, key)
    print(decryptedPlaintext)


encryptDecrypt()

print('=== Now lets show some cryptographic properties of the Caesar cipher')


def withWeakKey():
    print('--- Encrypting plaintext with a weak key is not a good idea')
    plaintext = 'Hello world!'
    # This is the weakest key of all, it does nothing
    weakKey = 0
    ciphertext = caesarEncrypt(plaintext, weakKey)
    print(ciphertext)  # just prints out the plaintext


withWeakKey();


def withoutDecrypt():
    print('--- Do we actually need caesarDecrypt at all?')
    plaintext = 'Hello world!'
    key = 3  # the original value for the Caesar cipher
    ciphertext = caesarEncrypt(plaintext, key)
    print(ciphertext)
    decryptionKey = 26 - key;  # reciprocal value
    decryptedPlaintext = caesarEncrypt(ciphertext, decryptionKey)
    print(decryptedPlaintext)  # performed decryption


withoutDecrypt()


def punnify():
    print('--- ROT 13 is the Caesar cipher with a given, reciprocal, weak key: 13')

    # The key is weak because double encryption will return the plaintext
    def rot13(pun):
        return caesarEncrypt(pun, 13)

    print('Q: How many marketing people does it take to change a light bulb?')
    obfuscated = 'N: V jvyy unir gb trg onpx gb lbh ba gung.'
    print(obfuscated)
    deobfuscated = rot13(obfuscated)
    print(deobfuscated)
    # We should not leak the pun, right? Lets obfuscate afterwards!
    obfuscatedAgain = rot13(deobfuscated)
    print(obfuscatedAgain)


punnify()


def bruteForceAndLength():
    print('--- Brute forcing is very easy as there are only 25 keys in the range [1..25]')
    # Note that AES-128 has 340,282,366,920,938,463,463,374,607,431,768,211,456 keys
    # and is therefore impossible to bruteforce (if the key is correctly generated)
    key = 10;
    plaintextToFind = 'Hello Maarten!'
    ciphertextToBruteForce = caesarEncrypt(plaintextToFind, key)
    for candidateKey in range(1, 25):
        bruteForcedPlaintext = caesarDecrypt(ciphertextToBruteForce, candidateKey)
        # lets assume the adversary knows 'Hello', but not the name
        if bruteForcedPlaintext.startswith('Hello'):
            print('key value: ' + str(candidateKey) + ' gives : ' + bruteForcedPlaintext)

    print('--- Length of plaintext usually not hidden')
    # Side channel attacks on ciphertext lengths are commonplace! Beware!
    if len(ciphertextToBruteForce) != len('Hello Stefan!'):
        print('The name is not Stefan (but could be Stephan)')


bruteForceAndLength()


def manInTheMiddle():
    print('--- Ciphers are vulnerable to man-in-the-middle attacks')
    # Hint: do not directly use a cipher for transport security
    moneyTransfer = 'Give Maarten one euro'
    key = 1
    print(moneyTransfer)
    encryptedMoneyTransfer = caesarEncrypt(moneyTransfer, key)
    print(encryptedMoneyTransfer)
    # Man in the middle replaces third word with educated guess
    # (or tries different ciphertexts until success)
    encryptedMoneyTransferWords = encryptedMoneyTransfer.split(' ');
    encryptedMoneyTransferWords[2] = 'ufo'  # unidentified financial object
    modifiedEncryptedMoneyTransfer = ' '.join(encryptedMoneyTransferWords)
    print(modifiedEncryptedMoneyTransfer)
    decryptedMoneyTransfer = caesarDecrypt(modifiedEncryptedMoneyTransfer, key)
    print(decryptedMoneyTransfer)


manInTheMiddle()