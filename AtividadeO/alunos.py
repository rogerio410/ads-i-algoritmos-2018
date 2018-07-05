def main():
    n = int(input('Qtd de Alunos: '))

    soma_medias = 0.0
    qtd_aprovados = 0
    qtd_reprovados = 0
    qtd_prova_final = 0

    for i in range(n):
        entrada = input('> ')
        dados = entrada.split()
        nota1 = float(dados[1])
        nota2 = float(dados[2])
        nota3 = float(dados[3])

        media_aluno = (nota1 + nota2 + nota3) / 3
        print('Media do aluno', media_aluno)

        if media_aluno >= 7:
            qtd_aprovados += 1
        elif media_aluno < 4:
            qtd_reprovados += 1
        else:
            qtd_prova_final += 1

        soma_medias += media_aluno

    media_turma = soma_medias / n

    print('Total de Alunos: ', n)
    print('Qtd Aprovados', qtd_aprovados)
    print('Qtd Reprovados', qtd_reprovados)
    print('Qtd Prova Final', qtd_prova_final)
    print('Media da turma %.1f' % media_turma )


if __name__ == '__main__':
    main()