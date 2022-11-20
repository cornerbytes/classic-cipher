from string import ascii_uppercase, ascii_lowercase

# define static variable
REV_ASCII_UPPER = ascii_uppercase[::-1]
REV_ASCII_LOWER = ascii_lowercase[::-1]

class atbash:

    def __init__(self):
        pass
    
    # add user_input
    def new(self, user_input: str):
        
        self.input = user_input
    
    # update user_input
    def update(self, update_user_input: str):

        self.input += update_user_input
    
    # encryption function
    def encrypt(self):

        result = ''

        for i in self.input:

            if i.isupper():
                result += REV_ASCII_UPPER[ ascii_uppercase.index(i) ]

            elif i.islower():
                result += REV_ASCII_LOWER[ ascii_lowercase.index(i) ]

            else: 
                result += i

        return result
    
    def decrypt(self):

        # since atbash cipher using the same algorithm for encryption and decryption
        # we can use the same function to encrypt the plaintext
        return self.encrypt()

    def __str__(self):

       return self.input