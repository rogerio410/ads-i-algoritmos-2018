def main():

    # INICIO
    linha = input()
    dia_inicio = int(linha.split()[1])

    linha = input()
    dados = linha.split(' : ')
    hora_inicio = int(dados[0])
    min_inicio = int(dados[1])
    seg_inicio = int(dados[2])

    # FIM
    linha = input()
    dia_fim = int(linha.split()[1])

    linha = input()
    dados = linha.split(' : ')
    hora_fim = int(dados[0])
    min_fim = int(dados[1])
    seg_fim = int(dados[2])

    # Transformar de Dia/hora/min/seg para segundos
    momento_inicio = seg_inicio + min_inicio*60 + hora_inicio*3600 + dia_inicio*86400
    momento_fim = seg_fim + min_fim*60 + hora_fim*3600 + dia_fim*86400

    duracao_em_segundos = momento_fim - momento_inicio

    # Transformar de Segundos para Dia/hora/min/seg
    duracao_dia = duracao_em_segundos // 86400
    resto = duracao_em_segundos % 86400

    duracao_horas = resto // 3600
    resto = resto % 3600

    duracao_minutos = resto // 60

    duracao_segundos = resto % 60

    # Escrever saída
    print(duracao_dia, 'dia(s)')
    print(duracao_horas, 'hora(s)')
    print(duracao_minutos, 'minuto(s)')
    print(duracao_segundos, 'segundo(s)')


if __name__ == '__main__':
    main()