#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='count_words',
    version='1.0',
    packages=['count_words'],
    author='JAYME, M. C.',
    author_email='murilochaves@ulbra.edu.br',
    description='Script com a funcionalidade de contar a frequência das palavras de um determinado texto',
    license='MIT License',
    keywords='frequencia palavras texto python',
    url='https://github.com/aleborba/packtrack',
    long_description='Script escrito em python que possui a funcionalidade de obter um determinado arquivo de texto e contar e mostrar a frequencia das palavras.',
    install_requires=[
        'unidecode >= 1.0.23',
    ],
)
