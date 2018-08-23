"""
Escreva suas funções aqui:
 - Tanto funcoes para funcionalidades do Menu;
 - Quanto funções auxiliares a estas.
"""


# ##### FUNCIONALIDADES MENU #####
def total_votos_validos(vereadores):
    total_votos = 0
    for vereador in vereadores:
        total_votos += vereador["total_votos"]
    return total_votos


def quociente_eleitoral(vereadores):
    quociente = total_votos_validos(vereadores) // 29
    return quociente


def total_votos_coligacao(vereadores, coligacoes):
    total_votos = 0
    for coligacao in coligacoes:
        for vereador in vereadores:
            if vereador["coligacao"] == coligacao["coligacao"]:
                total_votos += vereador["total_votos"]
        coligacao["total_votos"] = total_votos
        total_votos = 0
    return coligacoes


def total_vagas_qp(vereadores, coligacoes):
    for coligacao in coligacoes:
        coligacao["qtd_vagas"] = coligacao["total_votos"] // quociente_eleitoral(vereadores)
        coligacao["votos_sobra_total"] = coligacao["total_votos"] % quociente_eleitoral(vereadores)
    return coligacoes


def vagas_sobra(coligacoes):
    vaga_sobra = 5
    sobras = []
    while vaga_sobra > 0:
        for coligacao in coligacoes:
             sobras.append(coligacao["total_votos"] / (coligacao["qtd_vagas"] + 1))


'''def total(dados):
    print(cabecalho('Total de Coligacoes'), "Coligações: {}".format(len(dados)))


def lista_todos(dados):
    for registro in dados:
        print(registro)'''


# ### FUNCOES AUXILIARES ###
# Ex.: para ordenação, filtragens genéricas, reduções reaproveitáveis

def cabecalho(titulo):
    return ('***** ***** ELEIÇÕES TERESINA/2012 ***** *****\n'
            ' >> {} <<\n'.format(titulo))


def printa_coligacoes(coligacoes):
    if len(coligacoes) == 0:
        print("Não há coligacoes.")
    else:
        print("\n|       Coligação      | Total de votos | Qtd de vagas | Sobra total de votos |")
        print("---------------------------------------------------------------------------------")
        for coligacao in coligacoes:
            print("|" + coligacao["coligacao"] + ' ' * (22 - len(coligacao["coligacao"])), end='|')
            print(str(coligacao["total_votos"]) + ' ' * (16 - len(str(coligacao["total_votos"]))), end='|')
            print(str(coligacao["qtd_vagas"]) + ' ' * (13 - len(str(coligacao["qtd_vagas"]))), end='|')
            print(str(coligacao["votos_sobra_total"]) + ' ' * (22 - len(str(coligacao["votos_sobra_total"]))), end='|')
            print()
    print()
    input("Continuar... (Enter)")
    print("\n" * 5)


def printa_vereadores(vereadores):
    print("\n|               Nome              |  Número  |                     Partido                      |   "
          "Coligação   "
          "| Total de votos  |")
    print("--------------------------------------------------------------------------------------------------------"
          "---------------")
    for vereador in vereadores:
        print("|" + vereador["nome"] + ' ' * (33 - len(vereador["nome"])), end='|')
        print(str(vereador["numero"]) + ' ' * (10 - len(str(vereador["numero"]))), end='|')
        print(str(vereador["partido"]) + ' ' * (50 - len(str(vereador["partido"]))), end='|')
        print(str(vereador["coligacao"]) + ' ' * (24 - len(str(vereador["coligacao"]))), end='|')
        print(str(vereador["total_votos"]) + ' ' * (17 - len(str(vereador["total_votos"]))), end='|')
        print()
    print()
    input("Continuar... (Enter)")
    print("\n" * 5)


def bubble_sort(lista, chave=lambda x: x, inverso=False):
    fim = len(lista)-1
    trocou = True
    while trocou:
        trocou = False
        for i in range(fim):
            if (chave(lista[i]) > chave(lista[i + 1]) and not inverso) \
                    or (chave(lista[i]) < chave(lista[i + 1]) and inverso):
                troca(lista, i, i + 1)
                trocou = True
        fim -= 1


def ordenados_por(matriz, atributo, inverso=False):
    matriz2 = list(matriz)
    bubble_sort(matriz2, chave=lambda x: x[atributo], inverso=inverso)
    return matriz2


def troca(lista, a, b):
    aux = lista[a]
    lista[a] = lista[b]
    lista[b] = aux
