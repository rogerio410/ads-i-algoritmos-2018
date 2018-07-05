def main():
    n = int(input('Numeros de alunos: '))

    i = 1
    media = 0
    media_classe = 0
    cont_aprovados = 0
    cont_reprovados = 0
    cont_prova_final = 0
    
    while i <= n:
        linha = input().split()
        nome = str(linha[0])
        nota1 = int(linha[1])
        nota2 = int(linha[2])
        nota3 = int(linha[3])

        media_aluno = (nota1 + nota2 + nota3) / 3
        media_classe += media_aluno / n

        if media_aluno < 4:
            situacao = 'Reprovado'
            cont_reprovados += 1
            
        elif media_aluno < 7:
            situacao = 'Em Prova Final'
            cont_prova_final += 1
        else:
            situacao = 'Aprovado'
            cont_aprovados += 1

        print('Media de', nome, ': %.2f' %media_aluno, situacao)
    
        i += 1

    print('\nMedia da turma: %.2f' %media_classe)
    print('\nTotal de alunos Aprovados: ', cont_aprovados)
    print('\nTotal de alunos Em prova final: ', cont_prova_final)
    print('\nTotal de alunos Reprovados: ', cont_reprovados)
    
if __name__ == '__main__':
    main()
