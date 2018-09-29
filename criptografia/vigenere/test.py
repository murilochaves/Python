#coding:utf-8

characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
plaintext = 'Texto para criptografia'
key = 'turing'

plaintext = plaintext.upper()

for char in plaintext:
    print char