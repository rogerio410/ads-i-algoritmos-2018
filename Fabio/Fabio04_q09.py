def main():
    pontos_time_a = 0
    pontos_time_b = 0

    prova = int(input())
    qtd_nadadores = int(input())

    while prova != 0 or qtd_nadadores != 0:
        i = 1
        while i <= qtd_nadadores:
            print('Nadador ', i)
            nome = input('\tnome: ')
            classificacao = int(input('\tclass: '))
            tempo = input('\ttempo: ')
            time = input('\ttime: ')

            # descobrir os pontos
            if classificacao == 1: pontos = 9
            if classificacao == 2: pontos = 6
            if classificacao == 3: pontos = 4
            if classificacao == 4: pontos = 3

            if time == 'a':
                pontos_time_a += pontos
            else:
                pontos_time_b += pontos

            # convergencia
            i = i + 1

        # convergencia
        prova = int(input())
        qtd_nadadores = int(input())

    # Apuracao
    if pontos_time_a > pontos_time_b:
        campeao = 'Time A'
    elif pontos_time_b > pontos_time_a:
        campeao = 'Time B'
    else:
        campeao = 'Empate'


    print('Time A: ', pontos_time_a);
    print('Time B: ', pontos_time_b);
    print('Resultado: ', campeao)

if __name__ == '__main__':
    main()