def main():
    S = input()
    conta = 0
    j = 0
    compare = 'SOS'
    for i in S:

        if i != compare[j]:
            conta += 1
        j +=1
        if j == 3:
            j = 0

    print(conta)


if __name__ == '__main__':
    main()

