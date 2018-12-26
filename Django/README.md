# Django

Este repositório possui como objetivo armazenar alguns códigos escritos em Python referentes à qualquer tipo de coisa relacionada ao [Django](https://docs.djangoproject.com/pt-br/2.1/contents/).


## Preparação do Ambiente

### Python

A versão mais recente pode ser baixada e instalada pelo instalador obtido no próprio site do Python: https://www.python.org

### PIP

Caso não tenha PIP instalado:

```
$ sudo easy_install pip
```

Porém, poderemos usar o PIP3, que já vem instalado com o Python3+.

### Virtual Environment

Nada mais nada menos que um ambiente isolado de desenvolvimento. Isso possibilita isntalar bibliotecas separadas por projetos impedindo que conflitem com outras bibliotecas e versões de Python ou Django específicas.

Criando um ambiente isolado com Python3

```
$ python3 -m venv nomeProjeto
```

Ativar

```
$ source nomeProjeto/bin/activate
```

Desativar

```
$ (nomeProjeto) deactivate
```

### Django

> Ter uma atenção para mexer somente na virtualenv específica do projeto

```
$ (nomeProjeto) pip install django
```

**Obs**.: Durante a escrita deste tutorial foi utilizado o Django 2.1.2 com a dependência pytz 2018.6

### IDE (vsCode/PyCharm)

## Requirements
