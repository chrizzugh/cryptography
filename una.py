#pip install pycryptodome==3.4.3
#pip install torchtext==0.2.3

from Crypto.Util.number import getPrime
from random import randrange
from math import gcd

#generating key
bits = int(input("Enter bit length of the primes: "))
p = getPrime(bits)
q = getPrime(bits)
print('P is ', p)
print('Q is ', q)
n = p * q
print('N is ', n)
totientN = (p - 1) * (q - 1)
print('Totient of N is ', totientN)
e = randrange(1, totientN)
while True:
    e = randrange(1, totientN)
    if gcd(e, totientN) == 1 and pow(e, -1, totientN) != e:
        break
print('E is', e)

d = pow(e, -1, totientN)
print('D is ', d)
print('Public Key is (', e, ', ', n, ')')
print('Private Key is (', d, ', ', n, ')')
encryptedText = ''
decryptedText = ''

#encryption
message = input("Input message you want to encrypt: ")
encryptedMsg = [ord(c) for c in message]
cypheredText = print('Encrypted message is ',
                     ''.join(map(lambda x: str(x), encryptedMsg)))

#decryption
plaintext = [chr(pow(c, d, n)) for c in encryptedMsg]
decryptedText = print('Decrypted message is ', ''.join(plaintext))

#pow(char, d, n)

