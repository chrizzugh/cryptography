base = int(input("Enter base: "))
mod = int(input("Enter Modulus(should be PRIME NUMBER): "))
secret_keyA = int(input("Enter Alice secret key: "))
secret_keyB = int(input("Enter Bob secret key: "))


aliceNum = base ** secret_keyA % mod
bobNum = base ** secret_keyB % mod


shared_keyA = bobNum ** secret_keyA % mod
shared_keyB = aliceNum ** secret_keyB % mod


print("The shared key of Alice is: ",shared_keyA ," The shared key of Bob is: ",shared_keyB)
print("Bobs decryption key: ", aliceNum)

def xor_encrypt(shared_key):
    import os.path
    filename = input("Enter the filename you want to encrypt: ")   
    if os.path.isfile(filename):
        f = open(filename, mode = "r", encoding = "utf-8")
        encrypted_text = "" 
        while 1:
            char = f.read(1)
            if not char:
                break
            encrypted_char = ord(char) ^ shared_key
            encrypted_text = encrypted_text + chr(encrypted_char)
        output = input("Enter file you want to put the encrypted message: ")
        g = open(output, "w+")
        g.write(encrypted_text)
        print("The file has been encrypted!")
    else:
        print("File does not Exist!  ")

xor_encrypt(shared_keyA)
