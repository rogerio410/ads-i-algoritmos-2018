def main():
    #saida
    print("o valor inserido é igual a {}.".format(sum([int(y)*2**x for x,y in enumerate(input("digite um numero em binário: ")[::-1])])))



if __name__ == '__main__':
    main()
