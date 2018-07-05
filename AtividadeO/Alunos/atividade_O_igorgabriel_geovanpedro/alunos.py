def main():
    n = int(input('Enter: '))
    aprovados = 0
    reprovados = 0
    prova_final = 0
    for i in range(n):
        nome, nota1, nota2, nota3 = input('Nome e Notas: ').split()
        nome = str(nome)
        nota1 = int(nota1)
        nota2 = int(nota2)
        nota3 = int(nota3)
        media = (nota1 + nota2 + nota3) / 3
        if media >= 7:
            aprovados += 1
        elif 7 > media > 4:
            reprovados += 1
        else:
            prova_final += 1
    print('{} aprovados {} reprovados {} prova final'.format(aprovados, reprovados, prova_final))


if __name__ == '__main__':
    main()
