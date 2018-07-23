"""
Leia uma frase e gere uma nova frase,
duplicando cada caractere da frase digitada.
"""
# Bruno e Carlos

def main():
    frase = input()
    nova_frase = ''

    for i in range(len(frase)):
        nova_frase += 2 * frase[i]
    print(nova_frase)

# by PVF
# def main():
#     print("".join([i*2 for i in input()]))

if __name__ == '__main__':
    main()
