def main():
    #entrada
    alunos = int(input("Número de alunos: "))
    total = 0
    classe = 0
    boletim = ' '

    #processamento
    for i in range (alunos):
        for j in range (1, 4):
            nota = float(input("Digite a %d º nota do %d º aluno: " %(j, i+1)))
            total += nota
            media = total / 3
            media_classe = media / alunos
        print("A média do %d º aluno foi: %.2f" %(i+1, media))










if __name__ == '__main__':
    main()