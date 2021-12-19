import sys
from cryptography.fernet import Fernet

def getContents(path):
    """Returns the contents of the specified file as a binary string"""
    with open(path, "rb") as data:
        return data.read()
    
def generateKey(path):
    """Generate a key and save it to the specified file"""
    key = Fernet.generate_key()
    with open(path, "wb") as datafile:
        datafile.write(key)
        
def encryptFile(plainFile, keyFile=None):
    """Encrypts the file found at plainFile with key file keyFile. If keyFile is None, a new one is generated and stored in a new file."""
    if keyFile == None:
        # generate a key file now.
        generateKey(plainFile + ".key")
        keyFile = plainFile + ".key"
        
    # actually encrypt the file now    
    key = getContents(keyFile)
    f = Fernet(key)
    encrypted = f.encrypt(getContents(plainFile)) # encrypt the file's bytes

    with open(plainFile, "wb") as output:
        output.write(encrypted)
    
def decryptFile(cypherFile, keyFile, outputFileName = None):
    """Decrypt cypherFile using key held in keyFile. If outputFileName is None, the decrypted contents are written back into the original, encrypted file."""
    key = getContents(keyFile)
    f = Fernet(key)
    plaintext = f.decrypt(getContents(cypherFile))

    if outputFileName == None:
        outputFileName = cypherFile
    
    with open(outputFileName, "wb") as datafile:
        datafile.write(plaintext)
    
if __name__ == "__main__":
    print("Select operation:\nk - Generate a new key for encryption.\ne - Encrypt a file and optionally create a new key file.\nd - Decrypt a file using a key.")
    op = input("-> ")
    if op == "k":
        # generate a key.
        path = input("Enter key name: ")
        generateKey(path)
        print("The key is generated")
    elif op == "e":
        # encrypt a file.
        path = input("Enter plaintext file name: ")
        keyfile = input("Enter key file name (leave blank to generate new): ")
        if keyfile == '': keyfile = None

        encryptFile(path, keyfile)
        print("The file is encrypted.")

    elif op == "d":
        # decrypt a file
        path = input("Enter encrypted file name: ")
        keyfile = input("Enter key file name: ")

        decryptFile(path, keyfile)
        print("The file is decrypted.")
    else:
        print("Invalid operation ID.")

