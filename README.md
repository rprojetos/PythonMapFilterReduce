# Python

## MAP 
Executa uma função especifica para cada item em um iteravel.
#### Sintax
map(função, iteravel)

## FILTER 
Cada item de um iteravel é testado por uma função, onde são retornados os itens validados(True).
#### Sintax
filter(function, iterable)

## REDUCE 
Reduce é uma função da biblioteca functools, por isso deve ser importado a partir dela:
from functolls import reduce

#### Sintax
reduce(função, iteravel, valorInicial)
Ex:
reduce(lambda acc, item: acc + item, iteravel, valInicial)
acc = acumulador que se inicia com o valor inicial
item = iteração resultante do iteravel 
iteravel = uma lista ou tupla por exemplo
valInicial = valor inicial do aculador
