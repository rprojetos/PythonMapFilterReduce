import math
from functools import reduce

produtos = [
    {'nome': 'Produto1', 'preco': 48.30, 'peso_kg': 5.942, 'classificacao': ['D', '3']},
    {'nome': 'Produto2', 'preco': 28.49, 'peso_kg': 1.923, 'classificacao': ['A', '2']},
    {'nome': 'Produto3', 'preco': 12.34, 'peso_kg': 9.482, 'classificacao': ['C', '3']},
    {'nome': 'Produto4', 'preco': 54.72, 'peso_kg': 2.643, 'classificacao': ['D', '1']},
    {'nome': 'Produto5', 'preco': 10.30, 'peso_kg': 7.594, 'classificacao': ['B', '3']},
    {'nome': 'Produto6', 'preco': 91.35, 'peso_kg': 1.837, 'classificacao': ['B', '2']},
    {'nome': 'Produto7', 'preco': 73.10, 'peso_kg': 6.945, 'classificacao': ['A', '1']},
    {'nome': 'Produto8', 'preco': 36.50, 'peso_kg': 3.927, 'classificacao': ['C', '1']},
    {'nome': 'Produto9', 'preco': 15.48, 'peso_kg': 8.504, 'classificacao': ['E', '2']},
]

##############################################################################

# MAP
# 1)Separar o peso total:
peso_total = sum(list(map(lambda p: p['peso_kg'], produtos)))
print(peso_total)
#out>> 48.797

# 2)Preço total:
preco_total = sum(list(map(lambda p: p['preco'], produtos)))
print(preco_total)
#out>> 370.58000000000004

# 3)Passando o preço para 2 casas decimais
preco_total = math.floor(preco_total * 10 ** 2) / 10 ** 2
print(preco_total)
#out>> 370.58

# Map com list comprehension
map_list_comprehension = sum([p['peso_kg'] for p in produtos])
print(map_list_comprehension)
#out>> 48.797

##############################################################################

# FILTER
# Filtrar lista para os produtos com peso maior que 7 kg:
lista_acima_7 = list(filter(lambda p: p['peso_kg'] > 7, produtos))
print(lista_acima_7)
#out>> 
# [
# {'nome': 'Produto3', 'preco': 12.34, 'peso_kg': 9.482, 'classificacao': ['C', '3']}, 
# {'nome': 'Produto5', 'preco': 10.3, 'peso_kg': 7.594, 'classificacao': ['B', '3']}, 
# {'nome': 'Produto9', 'preco': 15.48, 'peso_kg': 8.504, 'classificacao': ['E', '2']}
# ]

# Filter com list comprehension
filtro_peso_acima_7 = [p for p in produtos if p['peso_kg'] > 7]
print(filtro_peso_acima_7)
#out>> 
# [
# {'nome': 'Produto3', 'preco': 12.34, 'peso_kg': 9.482, 'classificacao': ['C', '3']}, 
# {'nome': 'Produto5', 'preco': 10.3, 'peso_kg': 7.594, 'classificacao': ['B', '3']}, 
# {'nome': 'Produto9', 'preco': 15.48, 'peso_kg': 8.504, 'classificacao': ['E', '2']}
# ]

##############################################################################

# Filter e Map
filter_map_peso_acima_7 = list(map(lambda p: p['peso_kg'], filter(lambda p: p['peso_kg'] > 7, produtos)))
print(filter_map_peso_acima_7)
#out>> [9.482, 7.594, 8.504]

# Filter e Map com list comprehension
filtro_map_peso_acima_7_listComprehension = [p['peso_kg'] for p in produtos if p['peso_kg'] > 7]
print(filtro_map_peso_acima_7_listComprehension)
#out>> [9.482, 7.594, 8.504]

##############################################################################

# REDUCE
# Ex.: Reduzir a lista de preço, realizando uma somatória, para um valor total.
preco_total = reduce(lambda acc,p: acc + p['preco'], produtos, 0)
print(preco_total)
#out>> 370.58000000000004

reduce_list_comprehension = sum([p['preco'] for p in produtos])
print(reduce_list_comprehension)
#out>> 370.58000000000004


