def main():

    # entrada
        n = int(input("Digite o numero de alunos: "))

        # declaracao de variaveis
        aprovados = 0
        reprovados = 0
        prova_final = 0
        soma = 0

        for i in range(n):
            separador()
            nome = input("Digite o nome do aluno: ")
            n1 = float(input("Digite a nota n1: "))
            n2 = float(input("Digite a nota n2: "))
            n3 = float(input("Digite a nota n3: "))

            # processamento
            media = calcula_media(n1,n2,n3)
            soma += media
            print("Nome:",nome)
            print("media:",media)

            if media >= 7:
                print("Situação: Aprovado")
                aprovados += 1
            elif 7 > media >= 4:
                print("Situação: Prova Final")
                prova_final += 1
            else:
                print("Situação: Reprovado")
                reprovados += 1

        media_turma = soma/n
        separador()
        print("Media da turma:",media_turma)
        print("Existem %d de alunos aprovados" % aprovados)
        print("Existem %d de alunos reprovados" % reprovados)
        print("Existem %d de alunos de prova final" % prova_final)

def calcula_media(n1, n2, n3):
    return (n1 + n2 + n3)/3


def separador():
    print("============================================")

if __name__ == "__main__":
    main()
