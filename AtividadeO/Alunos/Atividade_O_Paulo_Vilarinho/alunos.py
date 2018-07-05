def main():
    #entrada
    quantidade_de_alunos = int(input("digite a quantidade de alunos na sala"))
    total_notas = 0
    total_aprovados = 0
    total_prova_final = 0
    total_reprovados = 0
    #processamento
    for i in range(quantidade_de_alunos):
        #entradas
        aluno = input()
        #processamento
        nome = aluno.split()[0]
        nota_1 = int(aluno.split()[1])
        nota_2 = int(aluno.split()[2])
        nota_3 = int(aluno.split()[3])
        media = (nota_1 + nota_2 + nota_3)/3
        total_notas += media
        if media >= 7:
            total_aprovados += 1
        elif media < 4 :
            total_reprovados += 1
        else :
            total_prova_final += 1
        #saida
        print("O aluno {} está com a média: {:.2f}".format(nome,media))

    media_classe = total_notas/quantidade_de_alunos
    print("A media da classe é {:.2f}".format(media_classe))
    print("Quantidade de aprovados é {}".format(total_aprovados))
    print("Quantidade de reprovados é {}".format(total_reprovados))
    print("Quantidade de prova final é {}".format(total_prova_final))

if __name__ == '__main__':
    main()
