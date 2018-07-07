def main():
    # entrada
    numero = int(input('Número de alunos: '))
    numaprov = 0
    numrepro = 0
    numprovfi = 0
    mediaclasse = 0
    #processamento #saida
    while numero != 0:
        nota1 = int(input('Nota 1 do Aluno: '))
        nota2 = int(input('Nota 2 do Aluno: '))
        nota3 = int(input('Nota 3 do Aluno: '))
        media_aluno = (nota1 + nota2 + nota3) / 3
        mediaclasse += (media_aluno * numero) / 3
        print('A media da classe é {}'.format(mediaclasse))
        if media_aluno >= 7:
            numaprov += 1
            print('Aprovado')
        elif 4 <= media_aluno < 7:
            numprovfi += 1
            print('Em Prova Final')
        else:
            numrepro += 1
            print('Reprovado')

        print('Numero de aprovados foi {}, prova final {} e reprovados {}'.format(numaprov,numprovfi,numrepro))
if __name__ =='__main__':
    main()