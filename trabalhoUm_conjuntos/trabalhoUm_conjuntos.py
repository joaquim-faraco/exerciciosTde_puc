import itertools
# JOAQUIM DOS ANJOS FARACO - TURMA 2 A - BACHARELADO EM CIÊNCIA DA COMPUTAÇÃO

# TRABALHO 1 - CONJUNTOS

# ATENÇÃO: por gentileza, observar que o arquivo que deseja que seja lido deve ser inserido na função main(),
# no final do código (explicação presente como comentario na função).

# função para ler os arquivos e armazenar:
def lerarquivo(nome_arquivo):
    with open(nome_arquivo, 'rt') as arquivo:
        conteudo = arquivo.readlines()

    return conteudo


# função que, lendo as linhas do arquivo, seleciona os valores necessarios
def ler_conjuntos(arquivo, tipo_operacao):
    linhas = []
    capturando = False

    for linha in arquivo:
        linha = linha.strip()
        if linha == tipo_operacao:
            capturando = True
            conjuntos = []
        elif capturando:
            conjuntos.append(linha)
            if len(conjuntos) == 2:
                linhas.append(conjuntos)
                capturando = False

    return linhas


# funcao que converte e formata os valores, selecionados e colocados em conjunto pela funcao ler_conjuntos,
# em conjuntos manipulaveis
def conversor_conjunto(string_conjunto):
    return set(map(str.strip, string_conjunto.split(',')))


# funcao que realiza uniao entre conjuntos
def unir(conjuntos):
    resultados = []

    for conjunto1, conjunto2 in conjuntos:
        conjunto1 = conversor_conjunto(conjunto1)
        conjunto2 = conversor_conjunto(conjunto2)

        resultado = conjunto1.union(conjunto2)

        resultado_formatado = f"União: conjunto 1 {conjunto1}, conjunto 2 {conjunto2}. Resultado: {resultado}"
        resultados.append(resultado_formatado)

    return resultados


# funcao que realiza interseção entre conjuntos
def intersecao(conjuntos):
    resultados = []
    for conjunto1, conjunto2 in conjuntos:
        conjunto1 = conversor_conjunto(conjunto1)
        conjunto2 = conversor_conjunto(conjunto2)

        resultado = conjunto1.intersection(conjunto2)

        resultado_formatado = f"Interseção: conjunto 1 {conjunto1}, conjunto 2 {conjunto2}. Resultado: {resultado}"
        resultados.append(resultado_formatado)

    return resultados


# funcao que encontra a diferenca entre os conjuntos
def diferenca(conjuntos):
    resultados = []
    for conjunto1, conjunto2 in conjuntos:
        conjunto1 = conversor_conjunto(conjunto1)
        conjunto2 = conversor_conjunto(conjunto2)

        resultado = conjunto1.difference(conjunto2)

        resultado_formatado = f"Diferença: conjunto 1 {conjunto1}, conjunto 2 {conjunto2}. Resultado: {resultado}"
        resultados.append(resultado_formatado)

    return resultados


# funcao que encontra a relação cartesiana entre os conjuntos
def cartesiano(conjuntos):
    resultados = []
    for conjunto1, conjunto2 in conjuntos:
        conjunto1 = conversor_conjunto(conjunto1)
        conjunto2 = conversor_conjunto(conjunto2)

        resultado = list(itertools.product(conjunto1,conjunto2))

        resultado_formatado = f"Cartesiano: conjunto 1 {conjunto1}, conjunto 2 {conjunto2}. Resultado: {resultado}"
        resultados.append(resultado_formatado)

    return resultados


def main():
    # Inserir na linha abaixo (como string) o nome do arquivo que deseja que seja lido (default = arquivo teste
    # meu):
    nome_arquivo = 'arquivoTres'
    arquivo_lido = lerarquivo(nome_arquivo)

    conjuntos_uniao = ler_conjuntos(arquivo_lido, 'U')
    conjuntos_intersecao = ler_conjuntos(arquivo_lido, 'I')
    conjuntos_diferenca = ler_conjuntos(arquivo_lido, 'D')
    conjuntos_cartesiano = ler_conjuntos(arquivo_lido, 'C')

    resultados_finais = [unir(conjuntos_uniao), intersecao(conjuntos_intersecao), diferenca(conjuntos_diferenca),
                         cartesiano(conjuntos_cartesiano)]

    for i in resultados_finais:
        for conjuntos in i:
            print(conjuntos)


main()