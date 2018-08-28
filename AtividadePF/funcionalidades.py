from ordenacao import bubble_sort
# ##### FUNCIONALIDADES MENU #####

def total(dados):
    print(cabecalho('Total de Alunos'), "Alunos: {}".format(len(dados)))


def lista_todos(dados):
    for registro in dados:
        print(registro)



# ### FUNCOES AUXILIARES ###
# Ex.: para ordenação, filtragens genéricas, reduções reaproveitáveis

def cabecalho(titulo):
    return ('***** ALUNOS PROF. R1 *****\n'
            ' >> {} <<\n'.format(titulo))
