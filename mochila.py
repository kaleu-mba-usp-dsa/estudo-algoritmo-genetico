import random

from functions import pega_total_peso, pega_total_valor, exibe_dados, sorteia_dois_diferentes

print('PROBLEMA MOCHILA')

# ### GERAR POPULACAO INICIAL ###
# Gera um grupo de X indivíduos para compor a população inicial
# Avaliar o peso de todos para definir se passam na restrição e
# Gera indivíduos o bastante até completar a geração.

param_max_geracoes = 15
param_numero_individuos = 10
param_percentual_chance_mutacao = 0.1
populacao = []

while len(populacao) < param_numero_individuos:
    # Vamos dificultar para o algoritmo aumentando para 80% a chance
    # dele iniciar um gene como zero, que é o ítem fora da mochila
    # Fiz isso porque os valores iniciais estavam muito altos e rapidamente
    # o algoritmo chega na solução
    cromossomo = [random.choice([0, 0, 0, 0, 0, 0, 0, 0, 1, 1]) for _ in range(9)]
    if pega_total_peso(cromossomo) <= 5000 :
        populacao.append(cromossomo)

print(f'Gerou população de {len(populacao)} indivíduos')

# ### MÉTODO QUE AVALIA MELHOR SOLUÇÃO ###
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

# Avalia população inicial para referência
avalia_fitness(populacao)

# ### EXECUTA GERAÇÕES ###
for i in range(param_max_geracoes):
    # ### SELECIONA PAIS PARA UMA NOVA RODADA ###
    ### Vou usar uma solução simples, pegando os 60% melhores
    ### E realizando cruzamentos aleatórios entre eles para gerar os novos 8
    ### Manterei os dois melhores da geração anterior como um processo de elitismo

    # Ordenar a população simplifica o elitismo e a seleção dos "melhores"
    populacao_ordenada = sorted(populacao, key=lambda item: pega_total_valor(item), reverse=True)

    # ### ELITISMO ###
    # Mantém o primeiro com melhor desempenho
    # Para não correr risco de degradar o resultado justamente no final
    # das gerações. O uso de dois ou 3 (20% ou 30%) fez com que
    # em várias situações o resultado estacionasse em 38 ou 39 pontos
    # Sem chegar ao ótimo conhecido de 41
    nova_populacao = [populacao_ordenada[0].copy()]

    # A variável repetições é uma saída de segurança
    # caso ao mexer nos parâmteros eu causasse um loop infinito aqui
    repeticoes = 0
    while len(nova_populacao) < param_numero_individuos and repeticoes < 100:
        repeticoes += 1

        # Sorteia pai e mãe, garantindo dois indivíduos diferentes
        a, b = sorteia_dois_diferentes(0, 5)
        pai = populacao_ordenada[a]
        mae = populacao_ordenada[b]

        # pega primeira parte do pai, sorteia o valor do meio e a última parte da mae
        filho = pai[:4] + [random.choice([pai[4], mae[4]])] + mae[5:]

        # ### MUTAÇÃO ###
        for index, gene in enumerate(filho):
            # Cada gene tem X% de chance de sofrer uma mudança
            if random.random() < param_percentual_chance_mutacao:
                filho[index] = 1 - gene

        # Avalia restrição do sistema
        peso = pega_total_peso(filho)
        if peso <= 5000:
            nova_populacao.append(filho)

    # Mostra resultado da geração
    print(f'Geração {i + 1}')
    print(f'Gerou nova população de {len(nova_populacao)} indivíduos')
    avalia_fitness(nova_populacao)

    # bora recomeçar
    populacao = nova_populacao

# Exibe melhor solução encontrada
exibe_dados(best_solution)