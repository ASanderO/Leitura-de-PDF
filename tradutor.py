import openai
from docx import Document
from collections import Counter
import re

# Insira sua API_KEY aqui
api_key = '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'


# Função para enviar uma pergunta ao ChatGPT
def perguntar_ao_chatgpt(pergunta, contexto):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Assunto do texto: {contexto}\nPergunta: {pergunta}",
        max_tokens=50,  # Ajuste o número de tokens conforme necessário
        api_key=api_key
    )

    resposta = response.choices[0].text.strip()
    return resposta


# Função para traduzir um texto
def traduzir_texto(texto, idioma_origem, idioma_destino):
    prompt = f"Traduza o seguinte texto do {idioma_origem} para o {idioma_destino}: '{texto}'"

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=50,  # Ajuste o número de tokens conforme necessário
        api_key=api_key
    )

    translated_text = response.choices[0].text.strip()
    return translated_text

def obter_palavras_mais_comuns(texto, n=10):
    words = re.findall(r'\b\w+\b', texto.lower())
    word_count = Counter(words)
    return word_count.most_common(n)

# Função para dividir o texto em partes menores
def dividir_texto(texto, max_tokens):
    partes = []
    tokens = texto.split()
    while tokens:
        parte = " ".join(tokens[:max_tokens])
        partes.append(parte)
        tokens = tokens[max_tokens:]
    return partes


# Ler o texto do arquivo .docx
nome_arquivo = 'saida_processado.docx'
doc = Document(nome_arquivo)

# Concatenar todos os parágrafos em um único texto
texto_completo = "\n".join([paragraph.text for paragraph in doc.paragraphs])

# Obter as 10 palavras mais comuns no texto
palavras_mais_comuns = obter_palavras_mais_comuns(texto_completo, n=10)

print("Palavras mais comuns no texto:")
for palavra, frequencia in palavras_mais_comuns:
    pass

# Criar uma pergunta com base nas palavras mais comuns
contexto = ", ".join([palavra for palavra, _ in palavras_mais_comuns])
pergunta = "Qual é o assunto do texto?"

# Enviar a pergunta ao ChatGPT
resposta_assunto = perguntar_ao_chatgpt(pergunta, contexto)
print(f"Assunto identificado: {resposta_assunto}")

# Dividir o texto para tradução em partes menores
partes_para_traduzir = dividir_texto(texto_completo,
                                     max_tokens=200)  # Dividir em partes de 200 tokens (ajuste conforme necessário)

# Realizar a tradução em duas requisições separadas
idioma_origem = "português"
idioma_destino = "inglês"

traducoes = []

for parte in partes_para_traduzir:
    traducao = traduzir_texto(parte, idioma_origem, idioma_destino)
    traducoes.append(traducao)

traducao_final = " ".join(traducoes)

print(f"Texto original:\n{texto_completo}")
print(f"Tradução para {idioma_destino}:\n{traducao_final}")