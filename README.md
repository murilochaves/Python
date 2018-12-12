# Python
Criado por **Murilo Chaves Jayme**

Repositório de alguns códigos amadores que farei em Python, afim de promover um melhor estudo e organização.

- **Motivação**:
    - Legibilidade e alto nível de abstração: sintaxe similar à linguagem natural, fácil leitura;
    - Multiplataforma: código fonte interpretado;
    - Multiparadigma: programação imperativa, funcional e orientada a objetos;
    - Tipagem dinâmica: as variáveis se ajustam aos valores recebidos;
    - Necessidade de identação: código limpo - não precisa usar '{}';
    - Diversos Frameworks: [web](https://www.djangoproject.com), [mobile](https://kivy.org/#home), [desktop](https://wiki.python.org/moin/TkInter);

## Códigos
- **[devMed](./devMed)**
    - [Olá Mundo](./devMed/olaMundo.py)
    - [Notas Ulbra v.1](./devMed/notasUlbrav1.py)
    - [Qual o nome do filme? (piadinha)](./devMed/nomeFilme.py)
    - [Operadores Aritméticos](./devMed/operadoresAritmeticos.py)
    - [Strings](./devMed/string.py)
    - [Operadores Lógicos](./devMed/operadoresLogicos.py)
    - [Manipular Arquivo](./devMed/Manipular%20Arquivo)
        - [Gravar e/ou criar arquivo](./devMed/Manipular%20Arquivo/gravarECriar.py)
        - [Ler arquivo](./devMed/Manipular%20Arquivo/ler.py)
        - [Adicionar informações em arquivo](./devMed/Manipular%20Arquivo/adicionar.py)
            - [Adicionar várias informações em arquivo](./devMed/Manipular%20Arquivo/adicionarVarios.py)
        - [TXT de exemplo](./devMed/Manipular%20Arquivo/teste.txt)

- **Inteligência Artificial**
    - Redes Neurais Artificiais
        - Neurônio de McCulloch-Pitts;
        - Aprendizado de Hebb;
        - Perceptron;
        - [Adaline](./Inteligência%20Artificial/Redes%20Neurais%20Artificiais/Adaline);
        - Kohonen;
        - Backpropagation;

## Configurar usuário do visual studio code para dar os commits como usuário
```
$ git config user.name "NomeDeUsuario"
$ git config user.email "email@provedor.com.br"
```

## Criar ambiente virtual de desenvolvimento isolado (virtualenv)
```
# criando pasta para atribuir projetos
$ mkdir nomeProjeto
$ cd nomeProjeto

# criando virtualenv
$ python3 -m venv nomeVirtualenv

# ativando virtualenv
$ source myvenv/bin/activate
```

## Criar uma alias para utilizar ll no terminal (OS X)
```
$ alias ll='ls -lG'
```

## Pacotes instalados em default do PIP
```
$ pip list
```

```
Package    Version
---------- -------
pip        10.0.1 
setuptools 39.0.1 
```

## LINTER

[PEP8](https://www.python.org/dev/peps/pep-0008/) é referente para as boas práticas do Python

``` $ pip install pep8 ```

ou

``` pip install pylint ```

Para habilitar o linter no visual studio code:

1. Abrir o Command Palette do Code (⇧⌘P)

2. Definir qual o modelo de linter à ser verificado, o PEP8 é as boas práticas dado pelo PyCon então, é uma boa de ser utilizado: Python: Selecionar Linter > PEP8

3. Caso deseja verificar se o Linter está habilitado, poderá verificar com: Python: Habilitar Linting > ON/OFF

4. O linter sempre será realizado quando salvar um arquivo .py, porém, se quiser verificar antes, basta executar: Python: Executar Linting

PS.: Maiores informações: [Linting - Visual Studio Code](https://code.visualstudio.com/docs/python/linting)

## Observações
- **Versão**: [Python](https://www.python.org) v.2.7.10
- **IDE**: [Microsoft Visual Studio Code](https://code.visualstudio.com) v.1.17.2
- **Execução**: [Terminal](https://support.apple.com/pt-br/guide/terminal/welcome) - macOS Sierra v.10.12.6

- Arquivo: .vscode adicionado somente para parar de aparecer: **Error** Linter pylint is not installed. (Não quero instalar pylint)

### Links legais:

- [Tutorial Django](https://tutorial.djangogirls.org/pt/django_installation/)
