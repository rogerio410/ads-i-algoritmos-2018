from manipulando_arquivos import *
from funcoes import *


def main():
    coligacoes = arquivo1()
    candidatos = arquivo2()

    menu = '\n01 - Consulta\n' \
           '02 - Consulta\n' \
           '03 - Consulta\n' \
           '04 - Consulta\n' \
           '05 - Consulta\n' \
           '06 - Consulta\n' \
           '00 - Sair\n'
    escolha = int(input(menu))

    while escolha != 0:
        if escolha == 1:
            print(somatoria_total_votos(candidatos))
        elif escolha == 2:
            total_votos = somatoria_total_votos(candidatos)
            print(cociente_eleitoral(total_votos))
        elif escolha == 3:
            coligacoes = arquivo1()
            coligacoes = total_votos_coligacoes(candidatos, coligacoes)
        elif escolha == 4:
            coligacoes = total_vagas_por_conciente(coligacoes, candidatos)
        elif escolha == 5:
            coligacoes = distribuindo_resto_vagas(coligacoes)
        elif escolha == 6:
            eleitos(coligacoes, candidatos)
        escolha = int(input(menu))


if __name__ == '__main__':
    main()
