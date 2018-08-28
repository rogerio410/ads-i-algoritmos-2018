def main():
	valor_disponibilizado = 80000
	meses, ultima_parcela = debito_devedor(valor_disponibilizado)

	print("Sao necessarios %d meses e o valor da ultima parcela eh %.1f" % (meses, ultima_parcela))
	

def debito_devedor(valor):
	saldo_devedor = valor
	juros_mensal_acrescentado = saldo_devedor * 0.0065

	aux = 0

	while saldo_devedor > 1200:
		saldo_devedor = saldo_devedor + juros_mensal_acrescentado - 1200
		aux += 1


	return aux, saldo_devedor




if __name__ == '__main__':
    main()
