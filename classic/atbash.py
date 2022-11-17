"""
(+)Example to encrypt a plaintext

    testing = atbash()
    testing.new('this is a plaintext!!!')
    testing.encrypt()
    print(testing)

    result : gsrh rh z kozrmgvcg!!!

(+)Example to decrypt a plaintext

    testing_2 = atbash()
    testing_2.new('gsrh rh z kozrmgvcg!!!')
    testing_2.decrypt()
    print(testing_2)

    result : this is a plaintext!!!
"""

from string import ascii_uppercase, ascii_lowercase

# define static variable
REV_ASCII_UPPER = ascii_uppercase[::-1]
REV_ASCII_LOWER = ascii_lowercase[::-1]

class atbash:

    def __init__(self):
        self.data = ""
    
    # add user_input
    def new(self, user_input: str):
        
        self.input = user_input
    
    # update user_input
    def update(self, update_user_input: str):

        self.input += update_user_input
    
    def decrypt(self):

        result = ''

        for i in self.input:

            if i.isupper():
                result += REV_ASCII_UPPER[ ascii_uppercase.index(i) ]

            elif i.islower():
                result += REV_ASCII_LOWER[ ascii_lowercase.index(i) ]

            else: 
                result += i

        self.data = result
    
    def encrypt(self):

        # since atbash cipher using the same algorithm for encryption and decryption
        # we can use the same function to encrypt the plaintext
        self.decrypt()

    # this one return the plaintext or ciphertext
    def __str__(self):

       return self.data