#Chrizza Mae Ecal
#BSCS3-B

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
publicKey = e, n
message = input("Input message you want to encrypt: ")
for char in message:
    encryptedText += '/' + str(pow(ord(char), e, n))
print('Encrypted Message is ',encryptedText.replace('/', ''))

#decryption
privateKey = d , n
plain_text = ''
encryptedText = list(encryptedText.split('/'))
encryptedText.remove('')

for char in encryptedText:
	plain_text += chr(pow(int(char), d, n))

print('Decrypted Message is ', plain_text)
