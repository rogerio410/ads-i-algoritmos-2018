#entrada

n1 = input(print("Nome do 1 aluno: "))
p1 = float(input(print("Nota 1: ")))
p2 = float(input(print("Nota 2: ")))
p3 = float(input(print("Nota 3: ")))

n2 = input(print("Nome do 2 aluno: "))
p11 = float(input(print("Nota 1: ")))
p22 = float(input(print("Nota 2: ")))
p33 = float(input(print("Nota 3: ")))

n3 = input(print("Nome do 3 aluno: "))
p111 = float(input(print("Nota 1: ")))
p222 = float(input(print("Nota 2: ")))
p333 = float(input(print("Nota 3: ")))

media = (p1 + p2 + p3)/3
media1 = (p11 + p22 + p33)/3
media2 = (p111 + p222 + p333)/3

if media <= 7:
    print("Aluno:%s:Aprovado"%n1)
elif media > 7 <= 4:
    print("Aluno:%s:Em prova final"%n1)
elif media <= 4:
    print("Aluno:%s:Reprovado"%n1)

if media1 <= 7:
    print("Aluno:%s:Aprovado"%n2)
elif media1 > 7 <= 4:
    print("Aluno:%s:Em prova final"%n2)
elif media1 <= 4:
    print("Aluno:%s:Reprovado"%n2)

if media2 <= 7:
    print("Aluno:%s:Aprovado"%n3)
elif media2 > 7 <= 4:
    print("Aluno:%s:Em prova final"%n3)
elif media2 <= 4:
    print("Aluno:%s:Reprovado"%n3)