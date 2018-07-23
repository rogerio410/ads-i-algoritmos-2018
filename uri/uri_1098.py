def main():
    i = 0
    while i <= 2:
        j1 = 1
        j2 = 2
        j3 = 3
        n = round(i, 1)
        if n % 1 == 0:
            if j1 % 1 == 0:
                print('I=%d J=%d' % (int(n), int(j1 + n)))
                print('I=%d J=%d' % (int(n), int(j2 + n)))
                print('I=%d J=%d' % (int(n), int(j3 + n)))
            else:
                print('I=%d J=%.1f' % (int(n), j1 + n))
                print('I=%d J=%.1f' % (int(n), j2 + n))
                print('I=%d J=%.1f' % (int(n), j3 + n))
        else:
            print('I=%.1f J=%.1f' % (n, j1+ n))
            print('I=%.1f J=%.1f' % (n, j2+ n))
            print('I=%.1f J=%.1f' % (n, j3+ n))

        i = i + 0.2


if __name__ == '__main__':
    main()