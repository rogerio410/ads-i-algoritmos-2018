def main():
    n = int(input('Número de alunos: '))
    aprovado = 0
    prova_final = 0
    reprovado = 0
    media_turma = 0.0
    for i in range(n):
        nome, n1, n2, n3 = input('Nome: '), int(input('Nota 1: ')), int(input('Nota 2: ')), int(input('Nota 3:'))
        media = (n1 + n2 + n3)/3
        media_turma = (media_turma + media)/2
        if media >= 7:
            aprovado += 1
        elif media < 4:
            reprovado += 1
        else:
            prova_final += 1
    print('Média da turma: {0:.2f}, aprovados: {1}, reprovados: {2} , em prova final: {3}'.format(media_turma, aprovado, reprovado, prova_final))


if __name__ == '__main__':
    main()