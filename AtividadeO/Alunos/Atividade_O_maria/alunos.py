def main():

    frase=input()
    caracter=""
    i=0
    while i< len(palavra):
        for palavra in frase:
            palavra=frase[i]
            if palavra.upper()not in palavra:
                caracter+=palavra
                i+=1
            else:
                caracter+="s"
        print(palavra)

if __name__=="__main__":
    main()
