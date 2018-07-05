def main():

    # entrada
    qnt_alunos = int(input('Quantidade de alunos: '))
    aprovados = 0
    reprovados = 0
    prova_final = 0

    # processamento
    for aluno in range(qnt_alunos):
        entrada = input()
        nome = str(entrada.split()[0])
        nota1 = float(entrada.split()[1])
        nota2 = float(entrada.split()[2])
        nota3 = float(entrada.split()[3])

        media = (nota1 + nota2 + nota3) / 3

        if media >= 7:
            aprovados += 1
        elif 4 <= media < 7:
            prova_final += 1
        else:
            reprovados += 1
    # saida
    print('Aprovados: {}'.format(aprovados))
    print('Prova final: {}'.format(prova_final))
    print('Reprovados: {}'.format(reprovados))


if __name__ == '__main__':
    main()

