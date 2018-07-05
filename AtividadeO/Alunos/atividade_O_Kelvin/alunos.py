def main():
    #entrada
    alunos = int(input())
    media_sala = 0
    aprovados = 0
    prova_final = 0
    reprovados = 0
    #processamento
    for i in range(1, alunos + 1):
        nome, n1, n2, n3 = input().split()
        n1 = int(n1)
        n2 = int(n2)
        n3 = int(n3)
        media = (n1 + n2 + n3) / 3
        media_sala += media
        if media >= 7:
            print('Aprovado')
            aprovados += 1
        elif media < 7 and media >= 4:
            print('Em prova final')
            prova_final += 1
        else:
            print('Reprovado')
            reprovados += 1
    #saida
    media_sala1 = media_sala / alunos
    print('===================')
    print('Média da sala: %.2f '%media_sala1)
    print('Quantidade de alunos aprovados:',aprovados)
    print('Quantidade de alunos em prova final', prova_final)
    print('Quantidade de alunos reprovados', reprovados)


if __name__ == '__main__':
    main()
