print("0 : Soma")
print("1 : Subtração")
print("2 : Multiplicação")
print("3 : Divisão")
print("4 : Exponenciação")
print("")

continuar = 0

while continuar != 1:
    print("Escolha a operação que deseja realizar:")
    opção = int(input())

    print("Qual o primeiro valor?")
    n1 = float(input())
    print("Qual o segund valor?")
    n2 = float(input())

    if opção == 0:
        print("{} + {} = {}".format(n1, n2, n1 + n2))
    elif opção == 1:
        print("{} - {} = {}".format(n1, n2, n1 - n2))
    elif opção == 2:
        print("{} x {} = {}".format(n1, n2, n1 * n2))
    elif opção == 3:
        print("{} / {} = {}".format(n1, n2, n1 / n2))
    elif opção == 4:
        print("{} ** {} = {}".format(n1, n2, n1 ** n2))

    print("Deseja fazer outra operação? 0 - SIM, 1 - NÂO")
    continuar = int(input())
