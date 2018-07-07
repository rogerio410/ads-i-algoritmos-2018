"""
05alunos.py
"""


def main():
    # entrada

    # processamento
    soma_da_media_de_todos_os_alunos = 0
    aprovados = 0
    prova_final = 0
    reprovados = 0
    for i in range(1, 4):
        aluno = input('\nNome do {}o. aluno: '.format(i))
        nota1 = float(input('Digite a 1a nota: '))
        nota2 = float(input('\rDigite a 2a nota: '))
        nota3 = float(input('Digite a 3a nota: '))
        media = (nota1 + nota2 + nota3) / 3
        print('Media do aluno ' + aluno + ': ' + str(media))

        soma_da_media_de_todos_os_alunos += media

        if media >= 7:
            aprovados += 1
        elif media >= 4:
            prova_final += 1
        else:
            reprovados += 1

    print('\nMedia das notas de todos os alunos da classe = %.2f' % float(soma_da_media_de_todos_os_alunos/3))
    print('--> Numero de alunos aprovados ......: ' + str(aprovados))
    print('--> Numero de alunos em prova final .: ' + str(prova_final))
    print('--> Numero de alunos reprovados .....: ' + str(reprovados)+'\n')


if __name__ == '__main__':
    main()
