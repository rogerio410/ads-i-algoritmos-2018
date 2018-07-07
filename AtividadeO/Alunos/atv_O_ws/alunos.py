def main():
    # Apresentação
    print('Esse programa verifica a situação academica de uma turma.')

    # Processamento
    somatoria_notas = 0
    total_alunos = 0
    aprovados = 0
    reprovados = 0
    prova_final = 0
    while True:
        # Entrada
        entrada = input('\nDigite o nome, a primeira, segunda e tereceira nota: ').split()
        total_alunos += 1
        nota1 = float(entrada[1])
        nota2 = float(entrada[2])
        nota3 = float(entrada[3])
        media = (nota1 + nota2 + nota3)/3
        somatoria_notas += media
        if media >= 7:
            aprovados += 1
        elif 4 <= media < 7:
            prova_final += 1
        elif media < 4:
            reprovados += 1
        continuar = int(input('\nDeseja continuar? [1 - SIM/ 0 - NÃO]:'))
        if continuar == 0:
            break
    media_classe = somatoria_notas/total_alunos

    # Saida
    print('Total de aprovados: {}'.format(aprovados))
    print('Em Prova Final : {}'.format(prova_final))
    print('Reprovados: {}'.format(reprovados))
    print('Média da classe: {}'.format(media_classe))


if __name__ == '__main__':
    main()
