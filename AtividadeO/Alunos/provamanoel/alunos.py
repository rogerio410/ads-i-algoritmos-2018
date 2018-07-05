def main():
    num  = int(input('Quantos alunos: '))
    quant_aprov = 0
    quant_repro = 0
    quant_prov = 0
    media_clas = 0
    media_alun = 0

    for i in range(num):
        digita = input("nome n1 n2 n3: ")
        aluno = digita.split()
        media_alun = (int(aluno[1])+int(aluno[2])+int(aluno[3]))/3
        media_clas += media_alun
        if media_alun >= 7:
        #    print('{} esta aprovado'.format(aluno[0]))
            quant_aprov += 1
        elif media_alun < 4:
         #   print('aluno reprovado'.format(aluno[0]))
            quant_repro += 1
        else:
         #   print('{} esta de prova final'.format(aluno[0]))
            quant_prov +=1


    media_clas = media_clas /num
    print('Media da classe é {}'.format(media_clas))
    print('{} aprovados. {} reprovados. {} de prova final'.format(quant_aprov,quant_repro,quant_prov))



if __name__ == '__main__':
    main()

