import random

from functions import pega_total_peso, pega_total_valor, exibe_dados, sorteia_dois_diferentes

print('PROBLEMA MOCHILA')

# ### GERAR POPULACAO ###
# Gerar um grupo de X indivíduos para compor a população inicial
# Avaliar o peso de todos para definir se passam na restrição e
# Gerar indivíduos o bastante até completar a geração.

param_numero_individuos = 10
param_percentual_chance_mutacao = 0.1
populacao = []

while len(populacao) < param_numero_individuos:
    cromossomo = [random.randint(0,1) for _ in range(9)]
    if pega_total_peso(cromossomo) <= 5000 :
        populacao.append(cromossomo)

print(f'Gerou população de {len(populacao)} indivíduos')

# ### AVALIA MELHOR SOLUÇÃO ###
geracoes = []
fitness = 0
best_solution = None

def avalia_fitness(_populacao):
    global fitness
    global best_solution

    _valores = []
    for i in _populacao:
        valor = pega_total_valor(i)
        _valores.append(valor)
        if valor > fitness:
            fitness = valor
            best_solution = i

    print(f'Fitness +alto: {fitness}')
    print(f'Média Valores: {sum(_valores) / len(_valores):2f}')
    print('')

avalia_fitness(populacao)

max_geracoes = 10
for i in range(max_geracoes):
    # ### SELECIONA PAIS PARA UMA NOVA RODADA ###
    ### Vou usar uma solução simples, pegando os 60% melhores
    ### E realizando cruzamentos aleatórios entre eles para gerar os novos 8
    ### Manterei os dois melhores da geração anterior como um processo de elitismo

    populacao_ordenada = sorted(populacao, key=lambda item: pega_total_valor(item), reverse=True)
    nova_populacao = []
    # nova_populacao.append(populacao_ordenada[0].copy())
    # nova_populacao.append(populacao_ordenada[1].copy())

    repeticoes = 0
    while len(nova_populacao) < 10 and repeticoes < 100:
        repeticoes += 1

        a, b = sorteia_dois_diferentes(0, 5)
        pai = populacao_ordenada[a]
        mae = populacao_ordenada[b]

        # pega primeira parte do pai e segunda parte da mae
        filho = pai[:4] + [random.choice([pai[4], mae[4]])] + mae[5:]

        # Chance de mutação de 10%
        for index, gene in enumerate(filho):
            if random.random() < param_percentual_chance_mutacao:
                filho[index] = 1 - gene

        peso = pega_total_peso(filho)

        if peso <= 5000:
            nova_populacao.append(filho)

    print(f'Geração {i + 1}')
    print(f'Gerou nova população de {len(nova_populacao)} indivíduos')
    avalia_fitness(nova_populacao)
    populacao = nova_populacao

exibe_dados(best_solution)