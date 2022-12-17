from random import randint

def GeraCPF():
    cpf = []
    for x in range(9):
        cpf.append(randint(0,9))
    return cpf

def JuntarNumeros(x):
    novo = ""
    for cont in range(9):
        novo += str(x[cont])


def CalculaDigitos(x):
    p1 = [11,10,9,8,7,6,5,4,3,2]
    novo = 0

    "Calculando primeiro digito"
    for cont in range(len(x)):
        novo = novo + (p1[cont + 1] * x[cont])
    novo = novo % 11
    if novo < 2:
        x.append(0)
    else:
        novo = 11 - novo
        x.append(novo)

    "Calculando segundo digito"
    novo = 0
    for cont in range(len(x)):
        novo = novo + (p1[cont] * x[cont])
    novo = novo % 11
    if novo < 2:
        x.append(0)
    else:
        novo = 11 - novo
        x.append(novo)
    return x


def ValidaCPF(cpf):
    novo = []

    valida = [CPF[-2], CPF[-1]]

    for x in range(len(cpf)-2):
        novo.append(cpf[x])

    y = CalculaDigitos(novo)
    verifica = [y[-2], y[-1]]
    if valida == verifica:
        print(" ")
        print("CPF Verdadeiro")
        print(" ")
    else:
        print(" ")
        print("CPF Falso")
        print(" ")


x = 0

while x == 0:
    decisao = input("""(1) Gerar CPF
(2) Verificar CPF
""")

    if decisao == '1':
        print(" ")
        CPF = (CalculaDigitos(GeraCPF()))
        print("CPF gerado: {}{}{}{}{}{}{}{}{}{}{}{}".format(CPF[0],CPF[1],CPF[2],CPF[3],CPF[4],CPF[5],CPF[6],CPF[7],CPF[8],"-",CPF[9],CPF[10]))

    elif decisao == '2':
        print(" ")
        EntraCPF = str(input("Entre com o CPF: ").replace("-", ""))
        CPF = []
        for x in range(len(EntraCPF)):
            CPF.append(eval(EntraCPF[x]))
        ValidaCPF(CPF)

    else:
        print(" ")
        print("Inválido")
        print(" ")

    escolha = input("Deseja Repetir? (S/N): ").replace("S", 's')
    if escolha != 's':
        break
    print(" ")