# Monty Python's Flying Circus

Este repositório possui como objetivo, armazenar uma simples raspagem de dados para fins acadêmicos.

## Objetivo:

**TODO**: criar uma lista dos atores que apareceram no programa de televisão *[Flying Circus do Monty Python](https://pt.wikipedia.org/wiki/Monty_Python%27s_Flying_Circus)*.

## Métodos:

1. Constituir um *dataset* (um arquivo .txt) nomeado de [flying_circus_cast.txt](./source_data/flying_circus_cast.txt) com as informações recolhidas da seção *[Series Cast](https://www.imdb.com/title/tt0063929/fullcredits/?ref_=tt_ov_st_sm)* (pode ser obtido do site [imdb.com](https://www.imdb.com))

2. Escrever uma função ```create_cast_list```, que recebe um nome de arquivo como entrada e retorna uma lista com o nome dos atores.

3. Reconhecer o padrão de arquivo, pois algumas informações podem estar desarrumadas sobre os papéis em que eles atuaram no programa.

> Cada linha está apresetada o seguinte padrão:

```name sobrename	name sobrename	...	 characters / ... n episodes, start_date-final_date```

4. **Hint**: Extrair apenas o nome e adicioná-lo a uma lista. Pode usar o método ```.split()``` para acessar cada linha.

## Saída:

É esperado algo parecido com:

```
Graham Chapman
Eric Idle
Terry Jones
Michael Palin
Terry Gilliam
John Cleese
Carol Cleveland
Ian Davidson
John Hughman
The Fred Tomlinson Singers
Connie Booth
Bob Raymond
Lyn Ashley
Rita Davies
Stanley Mason
David Ballantyne
Donna Reading
Peter Brett
Maureen Flanagan
Katya Wyeth
Frank Lester
Neil Innes
Dick Vosburgh
Sandra Richards
Julia Breck
Nicki Howorth
Jimmy Hill
Barry Cryer
Jeannette Wild
Marjorie Wilde
Marie Anderson
Caron Gardner
Nosher Powell
Carolae Donoghue
Vincent Wong
Helena Clayton
Nigel Jones
Roy Gunson
Daphne Davey
Stenson Falke
Alexander Curry
Frank Williams
Ralph Wood
Rosalind Bailey
Marion Mould
Sheila Sands
Richard Baker
Douglas Adams
Ewa Aulin
Reginald Bosanquet
Barbara Lindley
Roy Brent
Jonas Card
Tony Christopher
Beulah Hughes
Peter Kodak
Lulu
Jay Neill
Graham Skidmore
Ringo Starr
Fred Tomlinson
David Hamilton
Suzy Mandel
Peter Woods
```
