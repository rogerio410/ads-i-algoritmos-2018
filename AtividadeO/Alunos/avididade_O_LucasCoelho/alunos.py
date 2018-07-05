def main():


    n1 = int(input())
    n2 = int(input())
    n3 = int(input())

    nota1 = float(input())
    nota2 = float(input())
    nota3 = float(input())

    media = (nota1 + nota2 + nota3) / 3
    print('Media: {:.2f}'.format(media))

    if media > 7:
        print('Aprovado')
    elif media < 7 and media >= 4:
        print('Em Prova Final')
    elif media < 4:
        print('Reprovado')



if __name__=='__main__':
    main()
