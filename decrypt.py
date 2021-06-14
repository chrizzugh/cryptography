base = int(input("Enter base: "))
mod = int(input("Enter Modulus: "))
secret_keyB = int(input("Enter Bob secret key: "))
decryptionKey = int(input("Enter your decryption key: "))
shared_keyB = decryptionKey ** secret_keyB % mod


def xor_decrypt(shared_key):
    import os.path
    filename = input("Enter the Filename you want to decrypt: ")
    if os.path.isfile(filename):
        f = open(filename, mode = "r", encoding = "utf-8")
        decrypted_text = "" 
        while 1:
            char = f.read(1)
            if not char:
                break
            decrypted_char = ord(char) ^ shared_key
            decrypted_text = decrypted_text + chr(decrypted_char)
        output = input("Enter file you want to put the decrypted message: ")
        g = open(output, "w+")
        g.write(decrypted_text)
        print("The file has been decrypted!")
    else:
        print("File does not Exist!")

xor_decrypt(shared_keyB)
