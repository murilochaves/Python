# Gerador de Etiqueta Universal

Este documento tem como objetivo facilitar para o desenvolvedor sobre os possíveis informativos e erros que o sistema poderá apresentar, juntamente com o código de erro.

Assim, facilita para o desenvolvedor verificar no console qual é o 'inf' ou 'erro' presente no escopo do script, bastando copiar qual é q informação do console e indo diretamente para o fluxo respectivo.

## Informativos

inf-001 : Iniciando o processo das etiquetas
inf-002 : Versão atual do Gerador
inf-003 : Conteúdo dos argumentos passados via console
inf-004 : Iformação sobre os produtos capturados do JSON
inf-005 : Iformação sobre o ID do cliente capturados do JSON
inf-005 : Quantidade total de etiquetas à serem geradas pelo script

## Erros

erro-001 : Erro na manipulação do JSON

# Gerador de Etiquetas por Python

Este repositório tem como objetivo servir como backup de códigos funcionais de acordo com a progressão do desenvolvimento do código.

Modelo: PIMACO
Cor: Branca
Etiqueta: Retangular
Adesivo: Permanente
Tamanho: (MM) 21,2 x 38,2
Etiquetas por folha: 65
Etiquetas por envelope: 6500

Para desenvolvimento, criar uma virtualenv para não conflitar com as bibliotecas de outros projetos:
`$ python3 -m venv devLenvs`

Para ativar:
`$ source devLenvs/bin/activate`

Para desativar:
`$ (devLenvs) deactivate`

Para instalar as dependências:
`$ (devLenvs) pip install Pillow reportlab`

Requirements:
Python==3.7.0
Pillow==5.3.0
reportlab==3.5.9
