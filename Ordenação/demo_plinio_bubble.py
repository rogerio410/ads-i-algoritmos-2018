from plinio import plinio_sort
from bubble_sort import bubble_sort, bubble_sort_4_sequences


def main():
    numeros = [25, 20, 17, 25, 28, 19, 18, 25, 100, -6, 7, 110]
    aluno1 = ['Maria', 44, 'Feminino']
    aluno3 = ['Gui FA', 17, 'Masculino']
    aluno2 = ['Rogerio', 34, 'Masculino']

    alunos = [aluno1, aluno3, aluno2]

    print(alunos)
    #plinio_sort(numeros)
    #bubble_sort(numeros)
    #bubble_sort(numeros, reverse=True)
    #bubble_sort_4_sequences(alunos, 1)
    #q = lambda x:x[1]
    #bubble_sort(alunos, reverse=True, key=q)
    bubble_sort(alunos, reverse=False, key=lambda plinio:plinio[2])
    print(alunos)


def q(aluno):
    return aluno[1]


if __name__ == '__main__':
    main()