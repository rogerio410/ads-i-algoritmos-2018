def main():
    arquivo = open('alunos.txt')
    registros = []
    for linha in arquivo.readlines():
        registro = linha.strip().split(';')
        registros.append(registro)
    menu = 'xxxxxxxx ESCOLHA UMA OPÇÃO xxxxxxxx\n' \
           '01 - para resultadogeral\n' \
           '02 - resumo estatísticos e total por situacao \n' \
           '03 - para tabela ordenável\n' \
           '04 - para por parte do nome \n' \
           '05 - para busca por faixa de nota\n' \
           '06 - filtrar por situacao \n' \
           '07 - para media dos alunos que frequentaram o curso\n' \
           '0 - para sair'
    opcao = input(menu)

    while True:
        if opcao == '1':
            for i in range(len(registros)):
                nome_completo = registros[i][0].split()
                nome = nome_completo[0]
                sobrenome = nome_completo[len(nome_completo)-1]
                nota1 = float(registros[i][2])
                nota2 = float(registros[i][3])
                media = (nota1 + 2 * nota2)/ 3
                if registros[i][1] == 'A':
                    media += 0.5
                    if media >= 7.0:
                        situacao = 'APROVADO'
                    elif 4.0 <= media < 7.0:
                        situacao = 'PROVA FINAL'
                    elif media < 4.0:
                        situacao = 'REPROVADO'
                elif registros [i][1] == 'E':
                    situacao = 'EVADIDO'

                print(nome, ' ', sobrenome, nota1, nota2, media, situacao)

            opcao = input(menu)
        if opcao == '3':
            print('NÃO SEI')
            opcao = input(menu)
        if opcao == '2':
            evadidos = 0
            aprovados= 0
            reprovados = 0
            prova_final = 0
            total = len(registros)
            for i in range(len(registros)):
                nota1 = float(registros[i][2])
                nota2 = float(registros[i][3])
                media = (nota1 + 2 * nota2) / 3
                if registros[i][1] == 'A':
                    media += 0.5
                    if media >= 7.0:
                        aprovados += 1
                    elif 4.0 <= media < 7.0:
                        prova_final += 1
                    elif media < 4.0:
                        reprovados += 1
                elif registros[i][1] == 'E':
                    evadidos += 1
            aprovados_percentual = (aprovados / total) * 100
            evadidos_percentual = (evadidos/ total) * 100
            reprovados_percentual = (reprovados/ total) * 100
            prova_final_percentual = (prova_final / total) * 100
            print('APROVADOS = {}, em percentual: {:.2f} %'.format(aprovados, aprovados_percentual))
            print('REPROVADOS = {}, em percentual: {:.2f}%'.format(reprovados, reprovados_percentual))
            print('EVADIDOS = {}. Em percentual: {:.2f} %'.format(evadidos, evadidos_percentual))
            print('PROVA FINAL = {}. Em percentual: {:.2f} %'.format(prova_final, prova_final_percentual))
            opcao = (menu)

        if opcao == '4':
            parte_nome = input('digite nome ou parte do nome do aluno')
            for i in range(len(registros)):
                if parte_nome in registros[i][0]:
                    nome_completo = registros[i][0].split()
                    nome = nome_completo[0]
                    sobrenome = nome_completo[len(nome_completo)-1]
                    nota1 = float(registros[i][2])
                    nota2 = float(registros[i][3])
                    media = (nota1 + 2 * nota2)/ 3
                    situacao = registros[i][1]
                    print(nome, sobrenome, nota1, nota2, media, situacao)
                else:
                    print('ALUNO NÃO ENCONTRADO')

                opcao = input(menu)

        if opcao == '5':
            maxima = float(input('até qual nota? \n'))
            minima = float(input('acima de qual nota \n'))
            for i in range(len(registros)):
                nota1 = float(registros[i][2])
                nota2 = float(registros[i][3])
                media = (nota1 + 2 * nota2) / 3
                if  minima <= media <= maxima:
                    nome_completo = registros[i][0].split()
                    nome = nome_completo[0]
                    sobrenome = nome_completo[len(nome_completo)-1]
                    print(nome, sobrenome, media)
            opcao = input(menu)

        if opcao == '6':
            situacao = input("para listar APROVADOS, digite 'A'. Para Reprovados, digite 'R', para evadidos, 'E', para Prova final, PF'")
            if situacao == 'A':
                print('APROVADOS')
                for i in range(len(registros)):
                    if registros[i][1] == 'A':
                        nome_completo = registros[i][0].split()
                        nome = nome_completo[0]
                        sobrenome = nome_completo[len(nome_completo) - 1]
                        nota1 = float(registros[i][2])
                        nota2 = float(registros[i][3])
                        media = (nota1 + 2 * nota2)/ 3
                        media += .5
                        if media >= 7.0:
                            print(nome, sobrenome, media)
            if situacao =='R':
                print('REPROVADOS')
                for i in range(len(registros)):
                    if registros[i][1] == 'A':
                        nome_completo = registros[i][0].split()
                        nome = nome_completo[0]
                        sobrenome = nome_completo[len(nome_completo) - 1]
                        nota1 = float(registros[i][2])
                        nota2 = float(registros[i][3])
                        media = (nota1 + 2 * nota2)/ 3
                        media += .5
                        if media <= 4.0:
                            print(nome, sobrenome, media)
            if situacao =='PF':
                print('PROVA FINAL')
                for i in range(len(registros)):
                    if registros[i][1] == 'A':
                        nome_completo = registros[i][0].split()
                        nome = nome_completo[0]
                        sobrenome = nome_completo[len(nome_completo) - 1]
                        nota1 = float(registros[i][2])
                        nota2 = float(registros[i][3])
                        media = (nota1 + 2 * nota2)/ 3
                        media += .5
                        if  4.0 <= media <= 7.0:
                            print(nome, sobrenome, media)
            if situacao == 'E':
                print('EVADIDOS')
                for i in range(len(registros)):
                    if registros[i][1] == 'E':
                        nome_completo = registros[i][0].split()
                        nome = nome_completo[0]
                        sobrenome = nome_completo[len(nome_completo) - 1]
                        print(nome, sobrenome)
        opcao = input(menu)

        if opcao == '7':
            contador = 0
            soma_geral = 0
            for i in range(len(registros)):
                if registros[i][1] == 'A':
                    nota1 = float(registros[i][2])
                    nota2 = float(registros[i][3])
                    media = (nota1 + 2 * nota2) / 3
                    media += .5
                    soma_geral += media
                    contador += 1
            media_geral = soma_geral / contador
            print('A média geral dos alunos que não desistiram foi de {:.2F}'.format(media_geral))

        if opcao == '0':
            break

if __name__=='__main__':
    main()

