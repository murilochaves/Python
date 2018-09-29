#coding: utf-8

class Cesar:

    global characters
    global message

    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    message = ''

    def cript(self, plaintext, key):
        self.plaintext = plaintext.upper()
        self.key = key
        original_index = []
        cripto_index = []

        message = ''

        for char in self.plaintext:
            if char in characters:
                
                index_cript = characters.find(char)
                original_index.append(index_cript)

                index_cript = index_cript + self.key

                if index_cript >= len(characters):
                    index_cript = index_cript - len(characters)
                elif index_cript < 0:
                    index_cript = index_cript + len(characters)

                cripto_index.append(index_cript)

                message = message + characters[index_cript]

            else:
                message = message + char

                original_index.append(index_cript)
                cripto_index.append(index_cript)

        print ('Texto para criptografia: \n' + self.plaintext)
        print (original_index)

        print ('\nChave: ' + str(self.key))
        
        print ('\nMensagem criptografada: \n' + message)
        print (cripto_index)

    def cript_text_file(self, way, key):
        self.file_cript = open(way, 'r')
        self.key = key
        original_index = []
        cripto_index = []

        message = ''

        print ('Texto para criptografia: \n')
        for line in self.file_cript:
            
            self.plaintext = line.upper()
            print (self.plaintext)
            
            for char in self.plaintext:
                if char in characters:

                    index_cript = characters.find(char)
                    original_index.append(index_cript)

                    index_cript = index_cript + self.key

                    if index_cript >= len(characters):
                        index_cript = index_cript - len(characters)
                    elif index_cript < 0:
                        index_cript = index_cript + len(characters)

                    cripto_index.append(index_cript)

                    message = message + characters[index_cript]

                else:
                    message = message + char

                    original_index.append(index_cript)
                    cripto_index.append(index_cript)


        self.file_criptex = open('cesar/criptext.txt', 'w')

        self.file_criptex.write(message)
        self.file_criptex.close

        #print message

        self.file_cript.close

###########
## TESTE ##
###########

cripto = Cesar()

cripto.cript_text_file('cesar/plaintext.txt', 3)