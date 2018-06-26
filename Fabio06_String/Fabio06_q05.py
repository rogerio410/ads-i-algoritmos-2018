"""
Leia uma data no formato DD/MM/AAAA e
escreva o mês por extenso (DD de mês de AAAA).
"""
# by Brendom e Lucas

def main():
    data = input().split('/')
    dia = str(data[0])
    mes = str(data[1])
    ano = str(data[2])

    mes_escrito = ""
    if mes == '01':
        mes_escrito = "Janeiro"
    elif mes == '02':
        mes_escrito = "Fevereiro"
    elif mes == '03':
        mes_escrito = "Marco"
    elif mes == '04':
        mes_escrito = "Abril"
    elif mes == '05':
        mes_escrito = "Maio"
    elif mes == '06':
        mes_escrito = "Junho"
    elif mes == '07':
        mes_escrito = "Julho"
    elif mes == '08':
        mes_escrito = "Agosto"
    elif mes == '09':
        mes_escrito = "Setembro"
    elif mes == '10':
        mes_escrito = "Outubro"
    elif mes == '11':
        mes_escrito = "Novembro"
    elif mes == '12':
        mes_escrito = "Dezembro"

    print(dia, "de", mes_escrito, "de", ano)


if __name__ == '__main__':
    main()
