def main():

#entradas
    n = int(input('Alunos: '))
    for i in range(n):
        nome, nota1, nota2, nota3 = input('Nome e Notas: ').split()
        nome = str(nome)
        nota1 = int(nota1)
        nota2 = int(nota2)
        nota3 = int(nota3)
        media = (nota1 + nota2 + nota3) / 3
        if media >= 7:
            print('{} aprovado'.format(nome))
        elif media<7 and media>=4:
            print('{} prova final'.format(nome))
        else:
            print('{} reprovado'.format(nome))

#processamento

#saida


if __name__ == '__main__':
    main()
