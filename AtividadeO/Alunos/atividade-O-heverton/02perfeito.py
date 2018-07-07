"""
02.perfeito.py
"""


def main():
    # entrada
    n = int(input('Digite um numero: '))

    divisores = 0

    # processamento
    for i in range(1, n):
        if n % 1 == 0:
            divisores += 1
    # saida
    if divisores == n:
        print('{} eh perfeito.'.format(n))
    else:
        print('{} nao eh perfeito.'.format(n))


if __name__ == "__main__":
    main()
