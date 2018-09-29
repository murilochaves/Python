#coding: utf-8

plaintext = 'murilo 12'

characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

key = 3 #padrão da cifra de césar

cripto = ''

index = []

plaintext = plaintext.upper()

for char in plaintext:
    if char in characters:
        index_cript = characters.find(char)

        #criptografar
        index_cript = index_cript + key

        # tratamento de erros
        if index_cript >= len(characters):
            index_cript = index_cript - len(characters)
        elif index_cript < 0:
            index_cript = index_cript + len(characters)

        index.append(index_cript)

        cripto = cripto + characters[index_cript]

    else:
        cripto = cripto + char

        index.append(char)

print '\nTexto para criptografia: \n' + plaintext

print '\nChave: %d' % key
print index

print '\nTexto criptografado: \n' + cripto