import random

dados = {
    'itens': [
        'Barra de Cereal',
        'Casaco',
        'Tênis',
        'Celular',
        'Água',
        'Protetor Solar',
        'Protetor Labial',
        'Garrafas de oxigênio',
        'Máquina Fotográfica'
    ],
    'valor': [6, 7, 3, 2, 9, 5, 2, 10, 6],
    'peso': [200, 400, 400, 100, 1000, 200, 30, 3000, 500]
}

def check(itens):
    if len(itens) != 9:
        raise ValueError('Você deve sempre exibir um array de 9 ítens')

def pega_total_peso(itens):
    check(itens)
    return sum(peso for status, peso in zip(itens, dados['peso']) if status == 1)

def pega_total_valor(itens):
    check(itens)
    return sum(valor for status, valor in zip(itens, dados['valor']) if status == 1)

def exibe_dados(itens):
    if len(itens) != 9:
        raise ValueError('Você deve sempre exibir um array de 9 ítens')

    total_peso = 0
    total_valor = 0
    for index, value in enumerate(dados['itens']):
        if itens[index] == 0:
            continue

        valor = dados['valor'][index]
        peso = dados['peso'][index]

        total_valor += valor
        total_peso += peso

        print(f'{value}: {valor} ({peso}g)')

    print('#--------------------------#')
    print(f'Total Valor: {total_valor}')
    print(f'Total Peso: {total_peso}g')

def sorteia_dois_diferentes(start, end):
    a = random.randint(start, end)
    b = None
    while b is None or b == a:
        b = random.randint(start, end)

    return a, b