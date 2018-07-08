def main():
    mensagem = input()
    contador = 0
    contador_de_letra_errada = 0
    for i in range(len(mensagem)):
        if i % 3 == 0 and mensagem[i] != 'S':
            contador_de_letra_errada += 1
        elif i %


