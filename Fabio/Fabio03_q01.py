def main():
    while True:
        try:
            n = int(input())
            for i in range(1, n+1):
                print(i)
        except:
            break

if __name__ == '__main__':
    main()