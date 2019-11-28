"""declaring my class for colors, below are a  few different ones I'll use throughout my program"""
class text_colors:
    MAGENTA = '\033[85m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[94m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    UNDERLINE = '\033[4m'


"""here we are deciding weather we want to encrypt or decrypt a message, the getMode() will allow the user to type in what they want so either ecnrypt,e or decrypt, d. where we are starting a while loop, it will ask you to type in, as you can see we have input  and allows you to add a value to mode integer, you selected %s so it's looking for a text based answer, when selected it will print it back to you. return mode so return the value you have eclearntered."""
def getMode():  # definition called getmode, break program into sections
    while True:  # while loop start
        print('*' * 100 ) # used for a border prints * fifty times
        print("please chose the operation to be done: ")  # print on screen
        print(text_colors.GREEN + "\n ENCRYPT or e" + text_colors.ENDC)
        print(text_colors.RED + "\n DECRYPT or d" + text_colors.ENDC)
        print(text_colors.YELLOW + "\n BRUTEFORCE or b\n\n" + text_colors.ENDC)
        mode = input(">")  # allows user to input a value on screen
        print(text_colors.BLUE + "\nyou selected %s" % mode + text_colors.ENDC)  # reply what you typed
        print('*' * 100)
        # if mode in "encrypt e decrypt d".split():v
        return mode  # retunr the value of mode

"""Here is when we are asking for the user to type in their message, when we got the message we are then going to convert this, we will also tell the user what they sent as well."""
def getMessage():  # function for the message
    print("\nEnter your message here:")
    message = input("\n>")
    print(text_colors.BLUE + "\nyou selected %s" % message + text_colors.ENDC)
    print('*' * 100)
    return message  # retunr message

"""Here we are asking for the user to type their key into the terminal and when they do it will be added to the message to convert it from english to rubbish, the value of the key should be between the values of 1 - 26 any less or more and it simply won't work once types their message it fed back to them"""
def getKey():  # function for the key
    key = 0  # key is set to the value of zero
    while True:  # keeps looping intill a value has been entered
        print("enter the key number (%d)" % (26))  # asking to enter a key number value
        key = int(input("\n>"))  # raw input for the user to insert a number
        if (key >= 1 and key <= 26):  # if whats entered is greater than 1 and less then 26
            print(text_colors.BLUE + "\nyou selected %d" % key + text_colors.ENDC)  # print what user put
        print('*' * 100)
        return key  # return key value

"""this function does the encryptiona dn decryption in three parts mode sets the function to encryption mode or decryption mode, message is the plaintext (or ciphertext) to be encrypted (or decrypted), key is the key that is used in this cipher.in crypt the letters are called symbles, starts a for loop for message. is alpha is a string looking for alphabet, is upper looks for upper case letters and islower looks for lower, translated changes the encryption and decrypted charters in this string, if the symbol isn't a letter then it will either ignroe it and leave it same or shut down."""
def getTranslatedMessage(mode, message, key):
    if mode[0] == "d":  # checks if first letter in string is d for decrypt
        key = -key  # makes key a negavctie value for decryption
    translated = ''  # declaring translated
    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            translated += chr(num)
        else:

            translated += chr(num)
    return translated


"""The start of the program calls each of the three functions defined previously to get the mode, message, and key from the user. These three values are passed to getTranslatedMessage() whose return value (the translated string) is printed to the user.
These changes ask the user for the key if they arn't in bruteforce mode if they are it won't ask if thye are it goes from 1 to 26 showing all results"""

mode = getMode()  # looks back to mode to do the brute force
message = getMessage()  # message is getmessage
if mode[0] != "b":  # if mode is brute force
    key = getKey()  # get all the keys from 1 - 26

print("your translated text is")
if mode[0] != "b":  #
    print(text_colors.BLUE + (getTranslatedMessage(mode, message, key)) + text_colors.ENDC)
else:
    for key in range(1, 26 + 1):
        print(key, getTranslatedMessage("decrypt", message, key))

message = getMessage()
key = getKey()

print(text_colors.BLUE + "\nyour secret message is :" + text_colors.ENDC)
print(getTranslatedMessage(mode, message, key))
print('*' * 100)