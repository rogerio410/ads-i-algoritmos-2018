def main():
    #entrada
    numero_alunos = int(input('quantos alunos? \n'))
    aprovado = 0
    prova_final = 0
    reprovado = 0
    soma_de_notas = 0

    #processamento
    for aluno in range(numero_alunos):
        nome_nota1_nota2_nota3 = input('nome do aluno, nota1, nota2 e nota3')
        nome_nota1_nota2_nota3 = nome_nota1_nota2_nota3.split()
        aluno = nome_nota1_nota2_nota3[0]
        nota1 = nome_nota1_nota2_nota3[1]
        nota1 = float(nota1)
        nota2 = nome_nota1_nota2_nota3[2]
        nota2 = float(nota2)
        nota3 = nome_nota1_nota2_nota3[3]
        nota3 = float(nota3)
        soma_de_notas = soma_de_notas + nota1 + nota2 + nota3
        media = (nota1 + nota2 + nota3)/ 3
        if media >= 7.0:
            aprovado += 1
        elif media < 7.0 and media >= 4.0:
            prova_final += 1
        else:
            reprovado += 1
    media_classe = soma_de_notas /(numero_alunos * 3)

    #saída
    print('A media da classe foi {:.2f}'.format(media_classe))
    print('O número de aprovados foi ', aprovado)
    print('O número de reprovados foi ', reprovado)
    print('O número de alunos em prova final foi', prova_final)

if __name__=='__main__':
    main()