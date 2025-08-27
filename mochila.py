import random

from functions import pega_total_peso, pega_total_valor, exibe_dados

print('PROBLEMA MOCHILA')

# ### GERAR POPULACAO ###
# Gerar um grupo de X indivíduos para compor a população inicial
# Avaliar o peso de todos para definir se passam na restrição e
# Gerar indivíduos o bastante até completar a geração.

param_numero_individuos = 10
populacao = []

while len(populacao) < param_numero_individuos:
    cromossomo = [random.randint(0,1) for _ in range(9)]
    if pega_total_peso(cromossomo) <= 5000 :
        populacao.append(cromossomo)

print(f'Gerou população de {len(populacao)} indivíduos')

fitness = 0
best_solution = None

def avalia_fitness(_populacao):
    global fitness
    global best_solution

    for i in _populacao:
        valor = pega_total_valor(i)
        if valor > fitness:
            fitness = valor
            best_solution = i

    print(f'Fitness: {fitness}')
    exibe_dados(best_solution)
    print('')

avalia_fitness(populacao)
avalia_fitness(populacao)

