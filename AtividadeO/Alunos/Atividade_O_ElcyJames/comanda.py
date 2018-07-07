def main():
    print('## MENU ## \n1- Inserir Produtos\n2-Definir quantidade de pagantes\n3-Calcular conta\n4-Imprimir conta\n5-Confirmar pagamento')
    n = int(input())
    if n == 1:
        print(inserir())

def inserir():
    soma = 0
    s = input().split()
    quant = int(s[0])
    prod = str(s[1])
    if prod == 'T':
        soma = 29 * quant
    if prod == 'A':
        soma = 2 * quant
    if prod == 'C':
        soma = 8 * quant
    return soma


if __name__ == '__main__':
    main()