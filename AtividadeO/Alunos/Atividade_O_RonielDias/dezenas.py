from math import sqrt
def main():
	for i in range(1000, 10000):
		parte1 = i // 100
		parte2 = i % 100
		if(parte1+parte2 == sqrt(i)):
			print(i)

if __name__ == '__main__':
	main()



