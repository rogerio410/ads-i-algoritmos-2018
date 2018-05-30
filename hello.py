def main():
    count = 1
    print('Begin')

    while count <= 20:

        if eh_multiplo(count, 17):
            break

        if eh_multiplo(count, 13):
            count = count + 1
            continue

        print('Qdr', count, count ** 2)
        count = count + 1

    print('End')


def eh_multiplo(numero1, numero2):
    return numero1 % numero2 == 0


if __name__ == '__main__':
    main()
