import os

cwd = os.getcwd() # Current working directory, used because of VSC buffoonery

# Clear screen function for dialogue
def clearSc():
    os.system('cls' if os.name == 'nt' else "printf '\033c'")

global cipherText
cipherText = ""

cipherInts = [] # XOR-ed pairs' result gets added here


# Choosing an input method, file selections turns the whole file into a string 
# Encrypted text content should be written as a hexstring

def inputSelection(type):

    if type == "plaintext":
        clearSc()

        inputMethod = input("Do you want to input the text manually or use a txt file? (M / F)\n")
        if inputMethod == "M":
            clearSc()
            global inputString
            inputString = input("Text:")
        elif inputMethod == "F":
            clearSc()
            entries = os.listdir(cwd)
            for entry in entries:
                print(entry)
            inputFile = input("Choose input file 0-"+str(len(entries))+"\n")

            with open(entries[int(inputFile)], 'r') as file:
                inputString = file.read().replace('\n', '')
        else:
            inputSelection(type)

    if type == "key":
        clearSc()
        inputMethod = input("Do you want to input the key manually or use a txt file? (M / F)\n")
        if inputMethod == "M":
            clearSc()
            global inputKey
            inputKey= input("Key:")
        elif inputMethod == "F":
            clearSc()
            entries = os.listdir(cwd)
            for entry in entries:
                print(entry)
            inputFile = input("Choose input file 0-"+str(len(entries))+"\n")

            with open(entries[int(inputFile)], 'r') as file:
                inputKey = file.read().replace('\n', '')
        else:
            inputSelection(type)

    if type == "ciphertext":
        clearSc()
        inputMethod = input("Do you want to input the ciphertext manually or use a txt file? (M / F)\n")
        if inputMethod == "M":
            clearSc()
            global cipherText
            cipherText = input("Ciphertext(hexstring):")
        elif inputMethod == "F":
            clearSc()
            entries = os.listdir(cwd)
            for entry in entries:
                print(entry)
            inputFile = input("Choose input file 0-"+str(len(entries))+"\n")

            with open(entries[int(inputFile)], 'r') as file:
                cipherText = file.read().replace('\n', '')
        else:
            inputSelection(type)

def encryptXor():

    inputSelection("plaintext")
    inputSelection("key")
    global cipherText

    paddedKey = inputKey[:len(inputString)]
    inputArray = bytearray(inputString,"utf-8")
    keyArray = bytearray(paddedKey,"utf-8")

    for count, elem in enumerate(inputArray):
        value = elem ^ keyArray[count]
        cipherInts.append(value)

    # Turning integers into hexstring
    cipherText = bytearray(cipherInts).hex()
    print(cipherText)
    saveFile("encryption")

def decryptXor():

    inputSelection("ciphertext")
    inputSelection("key")
    global readableText
    decipheredText = []

    paddedKey = inputKey[:len(cipherText)] # Matching the input and key length
    cipherTextB = bytearray.fromhex(cipherText)
    keyArray = bytearray(paddedKey,"utf-8")
    
    for count, elem in enumerate(cipherTextB):
        value = elem ^ keyArray[count]
        decipheredText.append(value)
    readableText = ""
    for elem in decipheredText:
        readableText = readableText + chr(elem)
    print(readableText)
    saveFile("decryption")

def saveFile(method):
    
    if method == "encryption":
        confirm = input("Do you want to save the output? (Y / N)")
        if confirm == "Y":
             with open("encryptionOutput.txt", "w") as encryptFile:
                encryptFile.write(cipherText)
                encryptFile.close()
                print("File saved")
    elif method == "decryption":
        confirm = input("Do you want to save the output? (Y / N)")
        if confirm == "Y":
             with open("decryptionOutput.txt", "w") as encryptFile:
                encryptFile.write(readableText)
                encryptFile.close()
                print("File saved")

def programStart():

    def MethodChoice():
        clearSc()
        methodChoice = input("Do you want to encrypt or decrypt?(E / D) \n")
        
        if methodChoice == "E":
            encryptXor()
            
        elif methodChoice == "D":
            decryptXor()
        else:
            MethodChoice()
    MethodChoice()


programStart()