def main():
    # entrada
    num_alunos = int(input())

    # processamento, entrada
    media_classe = 0
    soma_media = 0
    aprovados = 0
    reprovados = 0
    prova_final = 0
    for i in range(num_alunos):
        nome, n1, n2, n3 = input().split()
        media = (int(n1) + int(n2) + int(n3)) / 3
        print("Media do aluno {}: {:.2f}" .format(nome, media))  # saída intermediária
        soma_media += media
        if media < 4:
            reprovados += 1
        elif media < 7:
            prova_final += 1
        else:
            aprovados += 1
    media_classe = soma_media / num_alunos

    # saida
    print("\nMédia da classe: {:.2f}" .format(media_classe))
    print("Aprovados:", aprovados)
    print("Prova final:", prova_final)
    print("Reprovados:", reprovados)


if __name__ == '__main__':
    main()
