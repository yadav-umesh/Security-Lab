keyMatrix = [[0] * 3 for i in range(3)]
messageVector = [[0] for i in range(3)] # Generate vector for the message
cipherMatrix = [[0] for i in range(3)] # Generate vector for the cipher

#generates the key matrix for the key string
def getKeyMatrix(key):
	k = 0
	for i in range(3):
		for j in range(3):
			keyMatrix[i][j] = ord(key[k]) % 65
			k += 1

def encrypt(messageVector):
	for i in range(3):
		for j in range(1):
			cipherMatrix[i][j] = 0
			for x in range(3):
				cipherMatrix[i][j] += (keyMatrix[i][x] *
									messageVector[x][j])
			cipherMatrix[i][j] = cipherMatrix[i][j] % 26

def HillCipher(message, key):
	getKeyMatrix(key)

	# Generate vector for the message
	for i in range(3):
		messageVector[i][0] = ord(message[i]) % 65

	encrypt(messageVector)

	#encrypted text from the encrypted vector
	CipherText = []
	for i in range(3):
		CipherText.append(chr(cipherMatrix[i][0] + 65))

	print("Ciphertext: ", "".join(CipherText))

def main():
	message=input("enter the message to be send:")
	key=input("enter the key value:")

	HillCipher(message, key)

if __name__ == "__main__":
	main()
















