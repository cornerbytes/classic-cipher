from string import ascii_lowercase as LOWERCASE 
from string import ascii_uppercase as UPPERCASE

class caesar:
    
    def __init__(self):
        self.data = "None"
    
    # add user_input
    def new(self, user_input: str, key: int = 26):
        self.input, self.key = user_input, key
    
    # update user_input
    def update(self, update_user_input: str):

        self.input += update_user_input
    
    def encrypt(self):

        result = ''
        for i in self.input:

            if i.isupper():
                result += UPPERCASE[ (UPPERCASE.index(i) + self.key) % 26]

            elif i.islower():
                result += LOWERCASE[ (LOWERCASE.index(i) + self.key) % 26]
            else:
                result += i

        self.data = result

    def decrypt(self):

        self.key = 26 - self.key
        self.encrypt()

        
    def __str__(self):

       return self.data
