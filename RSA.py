import math
import random


def isPrime(n):
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False

    return True


def GenerateE(e, phi):
    while e < phi:
        if math.gcd(e, phi) == 1:
            return e
        else:
            e += 1


def egcd(a, b):
    if a == 0:
        return b, 0, 1
    g, y, x = egcd(b % a, a)
    return g, x - (b // a) * y, y


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('No modular inverse')
    return x % m


def RSAEncrypt(text, e, n):
    Operation = list(text)
    for i in range(len(Operation)):
        if Operation[i].isupper():
            Operation[i] = chr(pow((ord(Operation[i]) - ord('A') + 1), e, n) % 26 + ord('A') - 1)
        else:
            Operation[i] = chr(pow((ord(Operation[i]) - ord('a') + 1), e, n) % 26 + ord('a') - 1)
    return Operation


def RSADecryption(text, d, n):
    Operation = list(text)
    for i in range(len(Operation)):
        if Operation[i].isupper():
            Operation[i] = chr(pow((ord(Operation[i]) - ord('A') + 1), d, n) % 26 + ord('A') - 1)

        else:
            Operation[i] = chr(pow((ord(Operation[i]) - ord('a') + 1), d, n) % 26 + ord('a') - 1)

    return Operation


class RSA:
    PlainText = " "
    CipherText = " "
    E = 2  # Public Key
    D = -1  # Private Key
    P = 2  # First Prime
    Q = 3  # Second Prime
    N = P * Q
    Phi = (P - 1) * (Q - 1)

    def GeneratePrimes(self):  # Generates 2 random Primes
        primes = [i for i in range(2, 10000) if isPrime(i)]
        self.P, self.Q = random.sample(primes, 2)
        self.N = self.P * self.Q
        self.Phi = (self.P - 1) * (self.Q - 1)
        self.E = GenerateE(self.E, self.Phi)
        self.D = modinv(self.E, self.Phi)

    def SetPrimes(self, p, q):  # Set the 2 Primes Manually
        if not isPrime(p) or not isPrime(q):
            raise Exception("These are not 2 prime numbers.")
        else:
            self.P = p
            self.Q = q
            self.N = self.P * self.Q
            self.Phi = (self.P - 1) * (self.Q - 1)
            self.E = GenerateE(self.E, self.Phi)
            self.D = modinv(self.E, self.Phi)

    def setPlain(self, text):
        self.PlainText = text
        self.CipherText = "".join(RSAEncrypt(text, self.E, self.N))

    def getCipher(self):
        return self.CipherText

    @staticmethod
    def DecryptCipher(text, d, n):
        return "".join(RSADecryption(text, d, n))

    @staticmethod
    def EncryptPlain(text, e, n):
        return "".join(RSAEncrypt(text, e, n))
