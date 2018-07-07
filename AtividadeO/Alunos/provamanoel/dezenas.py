def main():
    for i in range(1000,9999,1):
        dezen = str(i)[0:2] # SLICE NAO PERMITIDO
        unid = str(i)[2:4] # SLICE NAO PERMITIDO
        raiz1 = int(dezen)
        raiz2 = int(unid)
        if i**(1/2) == raiz1+raiz2:
            print(i)





if __name__ == '__main__':
    main()

