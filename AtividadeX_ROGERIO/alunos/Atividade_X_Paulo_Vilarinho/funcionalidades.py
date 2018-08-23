"""
Escreva suas funções aqui:
 - Tanto funcoes para funcionalidades do Menu;
 - Quanto funções auxiliares a estas.
"""


# ##### FUNCIONALIDADES MENU #####

def total(dados):
    print(cabecalho('Total de Coligacoes'), "Coligações: {}".format(len(dados)))


def lista_todos(dados,key = lambda x : x):
    for registro in dados:
        linha = ""
        dado = key(registro)
        for chave in dado:
            linha += " -> ".join([chave,str(registro[chave])]) + " | "
        print(linha)

def total_de_votos(dados,mostrar = True):
    votos = soma(dados,key = lambda x : int(x['total_votos']))
    if mostrar:
        print(cabecalho('Total de Votos'),"Votos: %d" %votos)
        return
    return votos

def quociente_eleitoral(dados,vagas,mostrar = True):
    votos = soma(dados,key = lambda x : int(x['total_votos']))
    quociente = votos//vagas
    if mostrar:
        print(cabecalho('Quociente Eleitoral'),"Quociente Eleitoral: %d" %quociente)
        return
    return quociente

def total_de_votos_por_coligacao(coligacoes,vereadores):
    for i in range(len(coligacoes)):
        coligados = filtro(vereadores,lambda x : x["coligacao"] == coligacoes[i]["coligacao"] )
        votos = soma(coligados,key = lambda x : int(x['total_votos']))
        coligacoes[i]["total_votos"] = votos

def total_de_vagas_por_quociente(coligacoes):
    quociente = quociente_eleitoral(coligacoes,29,mostrar = False)
    for i in range(len(coligacoes)):
        total_vagas = coligacoes[i]["total_votos"]//quociente
        coligacoes[i]['qtd_vagas'] = total_vagas
        coligacoes[i]['votos_sobra_total'] = coligacoes[i]["total_votos"]/(total_vagas + 1)

def vagas_sobraram(coligacoes,mostrar = True):
    total = 0
    for i in range(len(coligacoes)):
        total += coligacoes[i]['qtd_vagas']
    if mostrar:
        print("Sobraram %d vagas!" %(29 - total))
    return 29 - total


def preencher_vagas(coligacoes):
    lista_ordenada = bubble_sort(coligacoes, reverse = True, key = lambda x : int(x["votos_sobra_total"]))
    for i in range(vagas_sobraram(coligacoes,mostrar = False)):
        lista_ordenada[0]["qtd_vagas"] = int(lista_ordenada[0]["qtd_vagas"]) + 1
        lista_ordenada[0]["votos_sobra_total"] = int(lista_ordenada[0]["total_votos"])//(1 + int(lista_ordenada[0]["qtd_vagas"]))
        lista_ordenada = bubble_sort(lista_ordenada, reverse = True, key = lambda x : int(x["votos_sobra_total"]))
    return lista_ordenada

def vereadores_eleitos(coligacoes,vereadores):
    eleitos = []
    for i in range(len(coligacoes)):
        coligados = filtro(vereadores,lambda x : x["coligacao"] == coligacoes[i]["coligacao"] )
        coligados_ordenados = bubble_sort(coligados, reverse = True, key = lambda x : int(x['total_votos']))
        for vereador in coligados_ordenados[0:coligacoes[i]["qtd_vagas"]]:
            eleitos.append(vereador)
    return bubble_sort(eleitos,reverse = True , key = lambda x : int(x['total_votos']))

def vereadores_mais_votados(vereadores):
    vereadores_ordenados = bubble_sort(vereadores, reverse = True, key = lambda x : int(x['total_votos']))
    return vereadores_ordenados[0:29]

def vereadores_suplentes(coligacoes,vereadores,n):
    suplentes = []
    for i in range(len(coligacoes)):
        coligados = filtro(vereadores,lambda x : x["coligacao"] == coligacoes[i]["coligacao"] )
        coligados_ordenados = bubble_sort(coligados, reverse = True, key = lambda x : int(x['total_votos']))
        for vereador in coligados_ordenados[coligacoes[i]["qtd_vagas"]:n+coligacoes[i]["qtd_vagas"]]:
            suplentes.append(vereador)
    return suplentes

def gerar_partidos(vereadores):
    partidos_sem_chave = []
    partidos = []
    for vereador in vereadores:
        if vereador['partido'] not in partidos_sem_chave :
            partidos_sem_chave.append(vereador['partido'])
            partidos.append({"coligacao":vereador['partido'],"total_votos":0,"percentual_votos":0})
    for partido in partidos:
        for vereador in vereadores:
            if vereador['partido'] == partido['coligacao'] :
                partido['total_votos'] = int(vereador['total_votos']) + partido['total_votos']
        partido['percentual_votos'] = "%.2f" %((partido['total_votos']/395309)*100)
        partido['total_votos'] = "%d" %partido['total_votos']

    return partidos

# ### FUNCOES AUXILIARES ###
# Ex.: para ordenação, filtragens genéricas, reduções reaproveitáveis

def filtro(dados,condicao = lambda x : True):
    return [dado for dado in dados if condicao(dado)]

def cabecalho(titulo):
    return ('***** ***** ELEIÇÕES TERESINA/2012 ***** *****\n'
            ' >> {} <<\n'.format(titulo))

def soma(iteravel,key = lambda x : x):
    total = 0
    for i in range(len(iteravel)):
        total += key(iteravel[i])
    return total


def bubble_sort(iteravel, reverse = False,key = lambda x : x):
    lista = [i for i in iteravel]
    for i in range(len(lista)-1):
        swaped = 0
        for j in range(len(lista)-1 - i):
                if (key(lista[j]) > key(lista[j+1]) and not reverse) \
                    or(key(lista[j]) < key(lista[j+1]) and reverse):
                    swap(lista,j,j+1)
                    swaped +=1
        if swaped == 0 :
            return lista
    return lista

def swap(iteravel,a,b):
    aux = iteravel[a]
    iteravel[a] = iteravel[b]
    iteravel[b] = aux

def so_votos(dado):
    lista = {"coligacao":dado["coligacao"],"total_votos":dado["total_votos"]}
    return lista

def so_vagas(dado):
    lista = {"coligacao":dado["coligacao"],"qtd_vagas":dado["qtd_vagas"]}
    return lista

def so_porcentagem(dado):
    lista = {"coligacao":dado["coligacao"],"percentual_votos":str(dado["percentual_votos"])}
    return lista
