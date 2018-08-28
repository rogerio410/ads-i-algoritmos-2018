def main():
    sDevedor = 80000
    parcela = 1200

    cont_parcelas = 0
    while(sDevedor > 0):

    	juros = 0.0065 * sDevedor
    	if(sDevedor+juros > 1200):
    		sDevedor = sDevedor + juros
    		#print(cont_parcelas, sDevedor, parcela, juros)
    		sDevedor = sDevedor - parcela
    		cont_parcelas = cont_parcelas+1
    	else:
    		parcela = sDevedor + juros
    		#print(cont_parcelas, parcela, parcela, juros)
    		sDevedor = sDevedor - parcela
    		cont_parcelas = cont_parcelas+1
    		ultima_parcela = parcela

    print("Quantidade de parcelas: ", cont_parcelas-1)
    print("Valor da ultima parcela: %.2f" % parcela)

if __name__ == '__main__':
    main()