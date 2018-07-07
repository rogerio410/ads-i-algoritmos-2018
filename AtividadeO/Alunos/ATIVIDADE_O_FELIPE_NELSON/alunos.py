def main():

    numero_alunos = int(input('Digite o número de alunos: '))
    aprovados = 0
    reprovados = 0
    prova_final = 0
    somatorio_medias = 0

    for aluno in range(numero_alunos):
        nome, nota1, nota2, nota3 = input('Digite o nome e as três notas: ').split()
        media_aluno = (float(nota1) + float(nota2) + float(nota3)) / 3
        if media_aluno >= 7:
            aprovados += 1
        elif 4 <= media_aluno: # <
            prova_final += 1
        else:
            reprovados += 1
        somatorio_medias += media_aluno

    media_classe = somatorio_medias / numero_alunos

    print('Média da classe: %.2f' % media_classe)
    print('Número de Aprovados: %d' % aprovados)
    print('Número de Reprovados: %d' % reprovados)
    print('Número de Alunos de Prova Final: %d' % prova_final)


if __name__ == '__main__':
    main()
