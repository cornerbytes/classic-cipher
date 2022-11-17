"""
(+)Example to encrypt a plaintext

    testing = affine()
    testing.new('this is a plaintext!!!', 21, 123)
    testing.encrypt()
    print(testing)

    result : ckfh fh t wqtfgczic!!!

(+)Example to decrypt a plaintext

    testing_2 = affine()
    testing_2.new('ckfh fh t wqtfgczic!!!', 21, 123)
    testing_2.decrypt()
    print(testing_2)

    result : this is a plaintext!!!
"""

from math import gcd
from string import ascii_lowercase as LOWERCASE
from string import ascii_uppercase as UPPERCASE

class affine:

    
    def __init__(self):
        self.data = ''

    # add user_input, first key and second key
    def new(self, user_input: str, a: int, b: int):
        
        self.input, self.b = user_input, b

        # check if a is coprime with 26
        if gcd(a, 26) == 1:
            self.a = a

        # raise Exception if a is not coprime with 26
        else:
            raise Exception('A is not coprime with 26')
        
    # update user input
    def update(self, update_user_input: str):
        self.input += update_user_input
    
    # this one from pycryptodome
    def inverse(self, u, v):
        
        u3, v3 = u, v
        u1, v1 = 1, 0
        while v3 > 0:
            q = u3 // v3
            u1, v1 = v1, u1 - v1*q
            u3, v3 = v3, u3 - v3*q
        while u1<0:
            u1 = u1 + v
        return u1

    # encryption function 
    def encrypt(self):

        result = ''

        for i in self.input:

            if i.isupper():
                result += UPPERCASE[ (self.a * UPPERCASE.index(i) + self.b) % 26 ]
            elif i.islower():
                result += LOWERCASE[ (self.a * LOWERCASE.index(i) + self.b) % 26 ]
            else:
                result += i

        self.data = result

    # decryption function
    def decrypt(self):

        result = ''

        pow_a_min_1 = self.inverse(self.a, 26)
        
        for i in self.input:

            if i.isupper():
                result += UPPERCASE[ ( pow_a_min_1 * (UPPERCASE.index(i) - self.b) ) % 26 ]
            elif i.islower():
                result += LOWERCASE[ ( pow_a_min_1 * (LOWERCASE.index(i) - self.b) ) % 26 ]
            else:
                result += i
        
        self.data = result

    # return the plaintext or ciphertext
    def __str__(self):
        return self.data