#alunos
#entradas
def main():
    print("Saudações...")
    n1 = input("Digite o nome do aluno: ")
    nota1 = float(input("Digite a primeira nota do aluno: "))
    nota2 = float(input("Digite a segunda nota do aluno: "))
    nota3 = float(input("Digite a terceira nota do aluno: "))
    media = (nota1+nota2+nota3)/3
    print("A média do aluno",n1,"é",media)

    


if __name__ == '__main__':
    main()
