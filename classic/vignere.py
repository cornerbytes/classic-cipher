# vignere
from string import ascii_lowercase as LOWERCASE
from string import ascii_uppercase as UPPERCASE

class vignere:

    def __init__(self):
        self.data = ''

    # add user_input, first key and second key
    def new(self, user_input: str, key: str):
        
        self.input = user_input

        # filter only alphabet as a user input
        self.clean_ciphertext = [i for i in self.input if i.isalpha()]

        # padding the key
        self.key = "".join([ key[i % len(key)] for i in range(len(self.clean_ciphertext)) ])

        print(self.clean_ciphertext, self.key)

    def unpadding(self, result: str):
        
        result = [i for i in result]
        
        for i in range(len(self.input)):

            if not self.input[i].isalpha():

                result.insert(i, self.input[i])
        
        return "".join(result)

    
    def encrypt(self):
        
        result = ''

        for i in range(len(self.clean_ciphertext)):

            if self.clean_ciphertext[i].isupper():
                result += UPPERCASE[ (UPPERCASE.index(self.clean_ciphertext[i]) + UPPERCASE.index(self.key[i])) %26]
            
            else:
                result += LOWERCASE[ (LOWERCASE.index(self.clean_ciphertext[i]) + UPPERCASE.index(self.key[i])) %26]
        
        #temp
        self.data = self.unpadding(result)
    
    def decrypt(self):
        
        result = ''

        for i in range(len(self.clean_ciphertext)):

            if self.clean_ciphertext[i].isupper():
                result += UPPERCASE[ (UPPERCASE.index(self.clean_ciphertext[i]) - UPPERCASE.index(self.key[i])) %26]
            
            else:
                result += LOWERCASE[ (LOWERCASE.index(self.clean_ciphertext[i]) - UPPERCASE.index(self.key[i])) %26]
        
        print(result)
        #temp
        self.data = self.unpadding(result)

    
        
    # update user input
    def update(self, update_user_input: str):
        self.input += update_user_input

    def __str__(self):
        return self.data