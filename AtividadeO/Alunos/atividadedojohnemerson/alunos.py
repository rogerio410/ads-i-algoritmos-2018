def main():
    # entrada
    soma_da_media_de_todos_da_classe = 0
    aprovados = 0
    prova_final = 0
    reprovados = 0

    n = int(input('numero de alunos: '))
    for i in range(1, n+1):
        aluno = input('nome do {}º aluno: '.format(i))
        nota1 = float(input('primeira nota: '))
        nota2 = float(input('segunda nota: '))
        nota3 = float(input('terceira nota: '))

    # processamento
        media = (nota1 + nota2 + nota3) / 3
        soma_da_media_de_todos_da_classe += media
        if media >= 7:
            aprovados += 1
        elif media >= 4:
            prova_final += 1
        else:
            reprovados += 1

    # saida
        print('media do aluno = {}'.format(media))
    print()
    print('media da classe = {}'.format(soma_da_media_de_todos_da_classe / n))
    print('numero de aprovados = {}'.format(aprovados))
    print('numero de reprovados = {}'.format(reprovados))
    print('numero de alunos em prova final = {}'.format(prova_final))


if __name__ == '__main__':
    main()
