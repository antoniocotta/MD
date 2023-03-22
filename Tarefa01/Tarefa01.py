import time

# Define o decorador de contador de tempo
def tempo_de_execucao(funcao):
    def wrapper(*args, **kwargs):
        # obtém o tempo atual antes da execução da função
        start_time = time.time()

        # executa a função original
        resultado = funcao(*args, **kwargs)

        # obtém o tempo atual após a execução da função
        end_time = time.time()

        # calcula o tempo de execução da função em segundos
        elapsed_time = end_time - start_time

        # imprime o tempo de execução da função
        print("Tempo de execução:", elapsed_time, "segundos" "\n")
        # retorna o resultado da função original
        return resultado

    return wrapper

@tempo_de_execucao
def RELBINARIA(conjunto):
    # abre o arquivo de texto para escrita
    with open("resultados.txt", "w") as f:
        # cria todas as relações binárias do conjunto e escreve no arquivo de texto
        for i in range(2**(len(conjunto)**2)):
            binario = bin(i)[2:].zfill(len(conjunto)**2)
            relacao = []
            for j in range(len(binario)):
                if binario[j] == "1":
                    relacao.append((conjunto[j // len(conjunto)], conjunto[j % len(conjunto)]))
            # escreve a relação binária no arquivo texto
            f.write(str(relacao) + " ")

            # verifica se a relação é simétrica, transitiva, reflexiva, de equivalência,
            # irreflexiva, função, função bijetora, função sobrejetora e função injetora
            simetrica = verifica_simetria(relacao)
            transitiva = verifica_transitividade(relacao)
            reflexiva = verifica_reflexividade(conjunto, relacao)
            equivalencia = verifica_equivalencia(conjunto, relacao)
            irreflexiva = verifica_irreflexividade(conjunto, relacao)
            funcao = verifica_funcao(relacao)
            bijetora = verifica_bijetora(conjunto, relacao)
            sobrejetora = verifica_sobrejetora(conjunto, relacao)
            injetora = verifica_injetora(relacao)

            # escreve a classificação da relação no arquivo texto
            classificacao = ""
            if simetrica:
                classificacao += "S"
            if transitiva:
                classificacao += "T"
            if reflexiva:
                classificacao += "R"
            if equivalencia:
                classificacao += "E"
            if irreflexiva:
                classificacao += "I"
            if funcao:
                classificacao += "Fu"
            if bijetora:
                classificacao += "Fb"
            if sobrejetora:
                classificacao += "Fs"
            if injetora:
                classificacao += "Fi"
            f.write(classificacao + "\n")
        
# Função que verifica se a relação é simétrica
def verifica_simetria(relacao):
    for par in relacao:
        if (par[1], par[0]) not in relacao:
            return False
    return True

# Função que verifica se a relação é transitiva
def verifica_transitividade(relacao):
    for par1 in relacao:
        for par2 in relacao:
            if par1[1] == par2[0]:
                if (par1[0], par2[1]) not in relacao:
                    return False
    return True

# Função que verifica se a relação é reflexiva
def verifica_reflexividade(conjunto, relacao):
    for elemento in conjunto:
        if (elemento, elemento) not in relacao:
            return False
    return True


# Função que verifica se a relação é de equivalência
def verifica_equivalencia(conjunto, relacao):
    if not verifica_reflexividade(conjunto, relacao):
        return False
    if not verifica_simetria(relacao):
        return False
    if not verifica_transitividade(relacao):
        return False
    return True


# Função que verifica se a relação é irreflexiva
def verifica_irreflexividade(conjunto, relacao):
    for elemento in conjunto:
        if (elemento, elemento) in relacao:
            return False
    return True


# Função que verifica se a relação é função
def verifica_funcao(relacao):
    for par1 in relacao:
        for par2 in relacao:
            if par1[0] == par2[0] and par1[1] != par2[1]:
                return False
    return True


# Função que verifica se a relação é função bijetora
def verifica_bijetora(conjunto, relacao):
    if not verifica_funcao(relacao):
        return False
    if len(relacao) != len(conjunto):
        return False
    range_relacao = [par[1] for par in relacao]
    for elemento in conjunto:
        if range_relacao.count(elemento) != 1:
            return False
    return True


# Função que verifica se a relação é função sobrejetora
def verifica_sobrejetora(conjunto, relacao):
    if not verifica_funcao(relacao):
        return False
    range_relacao = [par[1] for par in relacao]
    for elemento in conjunto:
        if elemento not in range_relacao:
            return False
    return True


# Função que verifica se a relação é função injetora
def verifica_injetora(relacao):
    for par1 in relacao:
        for par2 in relacao:
            if par1[1] == par2[1] and par1[0] != par2[0]:
                return False
    return True

#Função principal
def main():
    # recebe a quantidade de elementos do conjunto
    n = int(input("Digite a quantidade de elementos do conjunto (máximo 5): "))
    while n > 5:
        print("Quantidade excedida. Por favor, digite novamente.")
        n = int(input("Digite a quantidade de elementos do conjunto (máximo 5): "))
    # recebe os valores dos elementos do conjunto
    conjunto = []
    for i in range(n):
        elemento = input("Digite o valor do elemento {}: ".format(i+1))
        conjunto.append(elemento)
    RELBINARIA(conjunto)
    
#Executa a função principal
main()
