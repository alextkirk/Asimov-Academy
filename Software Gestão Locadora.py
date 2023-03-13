import os

def Listar_Carros(disponíveis):
    for i in range(len(disponíveis)):
        print("[{}] {} - R${} / dia".format(i, disponíveis[i][0], disponíveis[i][1]))

def Alugar_Carro(disponíveis):
        print("=" * 40)
        print("Escolha o código do Carro:")
        carro = int(input())
        print("Escolha quantos dias deseja alugar:")
        dias = int(input())
        print("Você escolheu o {} por {} dias".format(carros[carro][0], dias))
        print("O aluguel totalizaria R${}. Deseja alugar?\n".format(carros[carro][1] * dias))
        print("0 - SIM | 1 - Não")
        prosseguir = int(input())
        if prosseguir == 0:
            info = carros[carro]
            del carros[carro]
            return info

def Devolver_Carro(alugados):
    print("Segue a lista de Carros alugados. Qual deseja devolver?")
    for i in range(len(alugados)):
        print("[{}] {} - R${} / dia".format(i, alugados[i][0], alugados[i][1]))
    print("\nEscolha o código do carro que deseja devolver:")
    dev = int(input())
    carro = alugados[dev]
    del alugados[dev]
    print("Obrigado por devolver o {}".format(carro[0]))
    return carro
    

carros = [
    ['Chevrolet Tracker' , 120],
    ['Chevrolet Onix' , 90],
    ['Chevrolet Spin' , 150],
    ['Hyundai HB20' , 85],
    ['Hyundai Tuckson' , 120],
    ['Fiat Uno' , 60],
    ['Fiat Mobi' , 70],
    ['Fiat Pulse' , 130],
]

alugados = []

while True:
    os.system("cls")
    print("=" * 40)
    print("Bem-vindo à locadora de Carros!")
    print("=" * 40)
    print("O que deseja fazer?")
    print("0 - Mostrar portifólio | 1 - Alugar Carro | 2 - Devolver Carro")
    opção = int(input())

    if opção == 0: #Mostrar lista de Carros Disponíveis
        os.system("cls")
        Listar_Carros(carros)
    elif opção == 1: #Alugar Carro e Remover da lista de Disponíveis
        os.system("cls")
        Listar_Carros(carros)
        alugados.append(Alugar_Carro(carros))
    elif opção == 2:
        os.system("cls")
        carros.append(Devolver_Carro(alugados))
    else:
        print("Opção inválida! Por favor escolha novamente!")

    #Loop do projeto
    print('=' * 40)
    print("0 - Continuar | 1 - Sair")
    continuar = int(input())
    while continuar != 0 and continuar != 1:
        print("Opção inválida! Tente novamente!")
        print('=' * 40)
        print("0 - Continuar | 1 - Sair")
        continuar = int(input())

    if continuar == 1:
        break


