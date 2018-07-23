def main():


    num_bin=input()
    lista=list(num_bin[0])
    i=0

    #for i in range(num_bin):

        
    pos1=int(num_bin[3])**2*[0]
    pos2=int(num_bin[2])**2*[1]
    pos3=int(num_bin[1])**2*[2]
    pos4=int(num_bin[0])**2*[3]
        
    decimal=(pos1 + pos2 + pos3 + pos4)
    print(decimal)
    i+=1


if __name__=="__main__":
    main()


             

