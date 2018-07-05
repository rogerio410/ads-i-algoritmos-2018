def main():
    numero_de_aluno = int(input('Numero de alunos: '))
    aprovado = 0
    prova_final = 0
    reprovado = 0
    soma_das_notas = 0

    for i in range(1, numero_de_aluno + 1):
        print('============================')
        print('Aluno %d' % i)

        nota1 = float(input('nota 1: '))
        nota2 = float(input('nota 2: '))
        nota3 = float(input('nota 3: '))

        media = (nota1 + nota2 + nota3) / 3

        print('Media do aluno igual a %.2f' % media)

        if media >= 7:
            print('Aluno aprovado')
            aprovado += 1
        elif media >= 4:
            print('Aluo em prova final')
            prova_final += 1
        else:
            print('Aluno reprovado')
            reprovado += 1

        soma_das_notas += media

    media_da_turma = soma_das_notas / numero_de_aluno

    print('============================')
    print('Total de alunos aprovados igual a %d' % aprovado)
    print('Total de alunos de prova final igual a %d' % prova_final)
    print('Total de alunos reprovados igual a %d' % reprovado)
    print('Media da turma igual a %.2f' % media_da_turma)


if __name__ == '__main__':
    main()
