from string import ascii_lowercase as LOWERCASE
from string import ascii_uppercase as UPPERCASE

class vigenere:

    def __init__(self):
        pass

    # add user_input, and key
    def new(self, user_input: str, key: str):
        
        self.input = user_input

        # filter only alphabet as a user input
        self.clean_ciphertext = [i for i in self.input if i.isalpha()]

        # padding the key 
        self.key = "".join([ key[i % len(key)] for i in range(len(self.clean_ciphertext)) ])

    # update user input
    def update(self, update_user_input: str):
        self.input += update_user_input

    # combine decrypted or encrypted string with non alphabet character from user_input as result
    def unpadding(self, result: str):
        
        result = [i for i in result]
        
        for idx, value in enumerate(self.input):

            if not value.isalpha():
                
                result.insert(idx, self.input[idx])
        
        return "".join(result)

    # encryption function
    def encrypt(self):
        
        result = ''

        for idx, value in enumerate(self.clean_ciphertext):

            if value.isupper():
                result += UPPERCASE[ (UPPERCASE.index(self.clean_ciphertext[idx]) + UPPERCASE.index(self.key[idx])) %26]
            
            else:
                result += LOWERCASE[ (LOWERCASE.index(self.clean_ciphertext[idx]) + UPPERCASE.index(self.key[idx])) %26]
        
        return self.unpadding(result)
    
    # decryption function
    def decrypt(self):
        
        result = ''

        for idx, value  in enumerate(self.clean_ciphertext):

            if value.isupper():
                result += UPPERCASE[ (UPPERCASE.index(self.clean_ciphertext[idx]) - UPPERCASE.index(self.key[idx])) %26]
            
            else:
                result += LOWERCASE[ (LOWERCASE.index(self.clean_ciphertext[idx]) - UPPERCASE.index(self.key[idx])) %26]
        
        return self.unpadding(result)
    
    def __str__(self):
        return self.input