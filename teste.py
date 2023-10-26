def criar_dicionario_de_frequencia(texto):
    palavras = texto.split()
    frequencia = {}
    for palavra in palavras:
        palavra = palavra.lower()
        if palavra in frequencia:
            frequencia[palavra] += 1
        else:
            frequencia[palavra] = 1
    return frequencia

def palavra_mais_frequente(dicionario):
    if not dicionario:
        return [], 0

    palavra_mais_comum = max(dicionario, key=dicionario.get)
    frequencia_mais_comum = dicionario[palavra_mais_comum]
    del dicionario[palavra_mais_comum]

    return [palavra_mais_comum], frequencia_mais_comum

def palavras_com_frequencia_igual_a(dicionario, x):
    resultado = []
    for palavra, frequencia in dicionario.items():
        if frequencia == x:
            resultado.append((palavra, frequencia))
    return resultado

# Leitura do arquivo de texto
nome_arquivo = input("Digite o nome do arquivo .txt: ")
try:
    with open(nome_arquivo, 'r') as arquivo:
        texto = arquivo.read()
except FileNotFoundError:
    print("Arquivo não encontrado.")
    exit(1)

dicionario_de_frequencia = criar_dicionario_de_frequencia(texto)
print("Dicionário de Frequência:")
print(dicionario_de_frequencia)

mais_frequente, frequencia_mais_frequente = palavra_mais_frequente(dicionario_de_frequencia)
print("\nPalavra(s) mais frequente(s):")
print(mais_frequente)
print("Frequência:", frequencia_mais_frequente)

x = int(input("\nDigite o valor de X para encontrar palavras com frequência igual a X: "))
palavras_com_frequencia_x = palavras_com_frequencia_igual_a(dicionario_de_frequencia, x)
print(f"\nPalavras com frequência igual a {x}:")
print(palavras_com_frequencia_x)
