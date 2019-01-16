#coding: utf-8

class Vigenere:

    global characters
    global message
    global key
    
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    message = ''
    key = ''

    def cript(self, plaintext, key):
        self.plaintext = plaintext.upper()
        self.key = key.upper()
        key_index = []
        plaintext_index = []
        message_cripto_index = []

        for char in self.key:
            if char in characters:
                index_key = characters.find(char)
                key_index.append(index_key)

        for char in self.plaintext:
            if char in characters:
                index_plaintext = characters.find(char)
                plaintext_index.append(index_plaintext)

        for char in self.plaintext:
            

        print '\n' + self.plaintext
        print plaintext_index
        print '\n' + self.key
        print key_index
        print '\n'



###########
## TESTE ##        
###########

cripto = Vigenere()

cripto.cript('Texto maior para criptografia', 'lacos que unem')