def main():
    n = int(input())
    s = 0

    for i in range(1, n + 1):
        s = s + 1/i

    print(s)

if __name__ == '__main__':
    main()