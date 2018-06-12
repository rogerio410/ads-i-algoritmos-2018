def main():
    n = int(input('Qts FB? '))
    fb1 = 0
    fb2 = 1
    print('%d %d' % (fb1, fb2), end=' ')

    qtd = n - 2
    for i in range(qtd):
        fb_atual = fb1 + fb2
        print(fb_atual, end=' ')

        fb1 = fb2
        fb2 = fb_atual

if __name__ == '__main__':
    main()