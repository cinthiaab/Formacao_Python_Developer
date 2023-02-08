# Mensagens que serão exibidas na tela

mensagem_inicial = " Seja Bem-vindo(a) ao Innovation Banco ".center(55, "-")
mensagem_final = """    
        Obrigado por usar nosso sistema bancário!
      O Innovation Banco trabalha pela sua confiança. \n""".center(
    224, "-")
mensagem_opcao_invalida = "\nOpção inválida."
mensagem_extrato = " VERIFIQUE SEU EXTRATO AQUI ".center(55, ".")
mensagem_depositar = " DEPOSITE AQUI ".center(55, ".")
mensagem_sacar = " SAQUE AQUI ".center(55, ".")
mensagem_valor_saque = "Informe o valor do saque: "
mensagem_valor_deposito = "Informe o valor do depósito: "
mensagem_deposito_invalido = "Depósito invalido"
mensagem_deposito_valido = "Depósito valido"
mensagem_saque_invalido = "Saque invalido"
mensagem_saque_valido = "Saque valido"
mensagem_reais = "R$ "
mensagem_nenhum_deposito = "Não há depósitos realizados nessa conta."
mensagem_extrato_deposito = "Depositos realizados nessa conta: "
mensagem_nenhum_saque = "Não há saques realizados nessa conta."
mensagem_extrato_saque = "Saques realizados nessa conta: "
mensagem_extrato_saldo = "O saldo da sua conta é "

menu = """

Escolha uma das opções abaixo:
    [1] - Verificar extrato
    [2] - Depositar
    [3] - Sacar
    [4] - Sair
    
Opção: """


# Funções que serão executadas dentro da função main()
def verificar_extrato(saques, depositos, saldo):
    print()
    print(mensagem_extrato)
    print()
    saldo = "{:.2f}".format(saldo)
    print(mensagem_extrato_saldo + mensagem_reais + saldo)
    print()

    if (len(saques) != 0):
        print(mensagem_extrato_saque)
        for saque in saques:
            saque = "{:.2f}".format(saque)
            print(mensagem_reais + saque)
    else:
        print(mensagem_nenhum_saque)

    print()

    if (len(depositos) != 0):
        print(mensagem_extrato_deposito)
        for deposito in depositos:
            deposito = "{:.2f}".format(deposito)
            print(mensagem_reais + deposito)
    else:
        print(mensagem_nenhum_deposito)


def depositar():
    print()
    print(mensagem_depositar)

    valor_depositado = float(input(mensagem_valor_deposito))

    if (valor_depositado > 0):
        print(mensagem_deposito_valido)
        return valor_depositado
    else:
        print(mensagem_deposito_invalido)
        return False


def sacar(quantidade_saques, saldo):
    print()
    print(mensagem_sacar)
    LIMITE_DE_SAQUES = 3
    VALOR_LIMITE_POR_SAQUE = 500

    saque = float(input(mensagem_valor_saque))
    if saque <= VALOR_LIMITE_POR_SAQUE and quantidade_saques < LIMITE_DE_SAQUES and (saldo-saque) >= 0 and saque > 0:
        print(mensagem_saque_valido)
        return saque
    else:
        print(mensagem_saque_invalido)
        return False


# Função main() que executa todo o sistema bancário
def main():
    print()
    print(mensagem_inicial)

    opcao = int(input(menu))
    saldo = 0.0
    quantidade_saques = 0
    quantidade_depositos = 0
    saques = []
    depositos = []

    while (opcao != 4):
        if opcao == 1:
            verificar_extrato(saques, depositos, saldo)
        elif opcao == 2:
            deposito = depositar()
            if (deposito != False):
                saldo += deposito
                depositos.append(deposito)
                quantidade_depositos += 1
        elif opcao == 3:
            saque = sacar(quantidade_saques, saldo)
            if (saque != False):
                saldo -= saque
                saques.append(saque)
                quantidade_saques += 1
        else:
            print(mensagem_opcao_invalida, end="")
        opcao = int(input(menu))

    print(mensagem_final)
