def main():
    #entrada
    numero1, numero2 = list(map(int,input().split()))

    #processamento
    if numero1 < numero2:
         numero1, numero2 = numero2, numero1

    r1,mdc=numero1%numero2,numero2                       
    while r1 != 0:
         r1,mdc=mdc%r1,r1
                         
    #saida
    print('Mdc de (%d %d) eh: %d'%(numero1,numero2,mdc))                     



if __name__ == '__main__':
   main()
