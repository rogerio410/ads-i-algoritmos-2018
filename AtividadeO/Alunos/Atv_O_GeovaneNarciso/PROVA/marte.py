def main():
    # entrada
    msg = input().upper()  # NAO PEMRITIDO

    # processamento
    s_na_msg = 0
    o_na_msg = 0
    alteradas = 0
    for i in range(len(msg)):
        if msg[i] == 'S':
            s_na_msg += 1
        if msg[i] == 'O':
            o_na_msg += 1
    alteradas = len(msg) - (s_na_msg + o_na_msg)

    # saida
    print("Letras alteradas:", alteradas)


if __name__ == '__main__':
    main()
