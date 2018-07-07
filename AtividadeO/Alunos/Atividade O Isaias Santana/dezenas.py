def main():
    numero = list(input())
    r = len(numero)
    t = 0
    part1 = ""
    part2 = ""
    for i in range(0, int(r/2)):
        t += i
        part1 += numero[i]
    for i in range(t+1, int(r)):
        part2 += numero[i]
    print(int(part1)+int(part2))


if __name__ == '__main__':
    main()