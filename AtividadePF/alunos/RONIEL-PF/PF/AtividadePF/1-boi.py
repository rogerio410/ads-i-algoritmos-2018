def main():
	qtd_fichas = int(input("Quantas fichas? "))

	boi = []
	cont_bois = 0
	for i in range(qtd_fichas):
		print("Boi %d" % (i+1))
		ident = int(input("ID: "))
		peso = float(input("Peso: "))

		aux = [ident, peso]
		boi.append(aux)
		cont_bois = cont_bois + 1
		print("-"*20)


	magro = 0
	gordo = 0
	media = 0
	for i in range(1, cont_bois):
		if(boi[i][1] < boi[magro][1]):
			magro = i
		if(boi[i][1] > boi[gordo][1]):
			gordo = i

		media = media + boi[i][1]

	media = media / cont_bois

	print("RELATORIO FINAL")
	print("Boi mais magro:")
	print("ID: %d" % boi[magro][0])
	print("Peso: %.1f" % boi[magro][1])
	print("Boi mais gordo:")
	print("ID: %d" % boi[gordo][0])
	print("Peso: %.1f" % boi[gordo][1])
	print("Media de peso: %d" % media)
	print("Quantidade de bois: %d" % cont_bois )

if __name__ == '__main__':
    main()