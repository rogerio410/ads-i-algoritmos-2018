def main():

    numero_alunos = int(input('Digite a quantidade de alunos: '))
    contador_aprovado, contador_prova_final, contador_reprovado = 0, 0, 0

    for aluno in range(numero_alunos):
        informacoes = input('Digite o nome, nota1, nota2 e nota3 do aluno: ').split(' ')
        nota1 = int(informacoes[1])
        nota2 = int(informacoes[2])
        nota3 = int(informacoes[3])
        media = (nota1 + nota2 + nota3) / 3

        if media >= 7:
            contador_aprovado += 1
        elif media >= 4:
            contador_prova_final += 1
        else:
            contador_reprovado += 1

    print('Numero de aprovados:', contador_aprovado)
    print('Numero de alunos em prova final:', contador_prova_final)
    print('Numero de reprovados:', contador_reprovado)


if __name__ == '__main__':
    main()
