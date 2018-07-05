classe = int(input("Digite o numero de alunos da classe (Turma): "))
contador_reprovados = 0
contador_aprovados = 0
contador_recuperacao = 0

for i in range(0,classe):
    aluno = str(input("Digite o nome do aluno: "))
    nota1 = float(input("Digite a primeira nota deste aluno: "))
    nota2 = float(input("Digite a segunda nota deste aluno: "))
    nota3 = float(input("Digite a terceira nota deste aluno: "))
    media = (nota1 + nota2 + nota3) / 3
    media_classe = ((nota1 + nota2 + nota3) * classe) / (3 * classe)
    print("{} -> Notas: {:.2f} , {:.2f} e {:.2f} // MEDIA = {:.2f}\n".format(aluno, nota1, nota2, nota3, media))
    if media >= 7:
        contador_aprovados += 1
        print("Aluno APROVADO!\n")

    elif media >= 4 and media < 7:
        contador_recuperacao += 1
        print("Aluno de RECUPERAÇÃO!\n")

    else:
        contador_reprovados += 1
        print("Aluno REPROVADO!\n")




print("\nA Turma tem {} alunos, e a média da turma foi {:.2f}.\nNa turma tivemos {} Aprovados, {} Alunos de Recuperação e {} Reprovados".format(classe, media_classe,contador_aprovados, contador_recuperacao, contador_reprovados))