def main():
    #entrada

    numero_de_alunos = int(input('Digite o número de alunos: '))

    #processamento

    notas_todos_os_alunos = 0
    total_alunos = 0
    numero_aprovados = 0
    numero_reprovados = 0
    numero_prova_final = 0

    for i in range(1, numero_de_alunos + 1):

        nota1 = float(input('Digite a nota da primeira prova: '))
        nota2 = float(input('Digite a nota da segunda prova: '))
        nota3 = float(input('Digite a nota da terceira prova: '))

        total_alunos = total_alunos + 3
        soma_notas = nota1 + nota2 + nota3
        media_alunos = (nota1 + nota2 + nota3) / 3
        notas_todos_os_alunos = notas_todos_os_alunos + soma_notas
        media_classe = notas_todos_os_alunos / total_alunos

        print('Média das notas dos aluno: {:.2f}'.format(media_alunos))

        if media_alunos >= 7:
            numero_aprovados += 1

        elif media_alunos < 7 and media_alunos >= 4:
            numero_prova_final += 1

        elif media_alunos < 4:
            numero_reprovados += 1

    #saída

    print('Média da clase: {:.2f}'.format(media_classe))
    print('Número de alunos aprovados: {}'.format(numero_aprovados))
    print('Número de alunos reprovados: {}'.format(numero_reprovados))
    print('Número de alunos em prova final: {}.'.format(numero_prova_final))


if __name__ == '__main__':
    main()