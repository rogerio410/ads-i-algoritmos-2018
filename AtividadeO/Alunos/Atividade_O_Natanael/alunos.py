def main():
    # entrada(Números de alunos na classe)
    n = int(input('Digite a quantidade de alunos na classe:'))

    # contadores
    aprovados = 0
    prova_final = 0
    reprovados = 0
    soma_notas_total = 0

    # processamento
    for i in range(n):
        # entrada(nome e notas dos alunos)
        nome, n1, n2, n3 = input('Digite o nome do aluno seguido de suas 3 notas:').split()
        n1, n2, n3 = int(n1), int(n2), int(n3)
        if (n1 + n2 + n3) / 3 >= 7:
            aprovados += 1
        elif 4 <= (n1 + n2 + n3) / 3 <= 7:
            prova_final += 1
        else:
            reprovados += 1

        soma_notas_total += n1 + n2 + n3

    media_da_classe = soma_notas_total / (n * 3)

    # saidas
    print('Dados:')
    print('\tAprovados-> %d\n\tEm prova final-> %d\n\tReprovados-> %d' % (aprovados, prova_final, reprovados))
    print('\tMédia da classe-> %.1f' % media_da_classe)


if __name__ == '__main__':
    main()
