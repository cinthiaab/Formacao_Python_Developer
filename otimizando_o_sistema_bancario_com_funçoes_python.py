# Constantes
AGENCIA = '0001'
LIMITE_DE_SAQUES = 3
VALOR_LIMITE_POR_SAQUE = 500

# Mensagens que serão exibidas na tela
mensagem_inicial = " Seja Bem-vindo(a) ao Innovation Banco ".center(75, "#")
mensagem_final = """
        Obrigado por usar nosso sistema bancário!
      O Innovation Banco trabalha pela sua confiança. \n""".center(
    224, "-")
mensagem_opcao_invalida = "\nOpção inválida."
mensagem_extrato = " VERIFIQUE SEU EXTRATO AQUI ".center(75, "=")
mensagem_depositar = " DEPOSITE AQUI ".center(75, "=")
mensagem_sacar = " SAQUE AQUI ".center(75, "=")
mensagem_valor_saque = "Informe o valor do saque: "
mensagem_valor_deposito = "Informe o valor do depósito: "
mensagem_deposito_invalido = "\n\tDepósito inválido\n"
mensagem_deposito_valido = "\n\tDepósito realizado com sucesso!\n"
mensagem_saque_invalido = "\n\tSaque inválido\n"
mensagem_saque_valido = "\n\tSaque realizado com sucesso!\n"
mensagem_reais = "R$ "
mensagem_nenhum_deposito = "Não há depósitos realizados nessa conta."
mensagem_extrato_deposito = "Depositos realizados nessa conta: "
mensagem_nenhum_saque = "Não há saques realizados nessa conta."
mensagem_extrato_saque = "Saques realizados nessa conta: "
mensagem_extrato_saldo = "O saldo da sua conta é "
mensagem_visualizacao_dados_usuario = " INFORMAÇÕES DO USUÁRIO ".center(
    75, "=")
mensagem_cadastro_usuario = " CADASTRO DO USUÁRIO ".center(
    75, "=")
mensagem_lista_de_contas_usuario = " CONTAS DO USUÁRIO ".center(75, "=")
mensagem_login_usuario = " LOGIN ".center(75, "-")
mensagem_dados_cpf = "Insira o seu CPF (apenas números): "
mensagem_dados_nome = "Insira o seu nome completo: "
mensagem_dados_data_de_nascimento = "Insira a sua data de nascimento: "
mensagem_dados_endereco = "Insira o seu endereço a seguir: "
mensagem_dados_logradouro = "Logradouro: "
mensagem_dados_bairro = "Bairro: "
mensagem_dados_numero = "Número: "
mensagem_dados_cidade = "Cidade: "
mensagem_dados_estado = "Estado (UF): "
mensagem_conta_criada = "\n\tConta criada com sucesso!\n"
mensagem_numero_da_conta = "Insira o número da conta que você deseja acessar: "
mensagem_conta_nao_existe = "Você não possui conta com esse número. Caso deseje voltar ao menu, digite -1."
mensagem_cadastro_sucesso = "Cadastro realizado com sucesso!"
mensagem_cpf_cadastrado = "Esse CPF já está cadastrado!"
mensagem_volta_para_o_menu = "Você será redirecionado para o menu principal. Faça o seu cadastro digitando o numero 1."
mensagem_cpf_ja_possui_cadastro = "Não encontramos esse CPF no nosso sistema. Tente novamente ou digite -1 para voltar para o menu inicial."
mensagem_nao_possui_contas = "Você não possui contas bancárias. Clique em 1 para criar."
mensagem_voltando_para_o_menu = "Voltando ao menu principal"

menu_principal = """
Escolha uma das opções abaixo:
    [1] - Cadastre-se
    [2] - Entre com o seu CPF
    [3] - Sair

Opção: """

menu_operaçoes = """

Escolha uma das opções abaixo:
    [1] - Verificar extrato
    [2] - Depositar
    [3] - Sacar
    [4] - Sair

Opção: """

menu_conta = """

Escolha uma das opções abaixo:
    [1] - Criar uma conta
    [2] - Listar minhas contas bancárias
    [3] - Acessar uma conta bancaria
    [4] - Sair

Opção: """


# funções utilizadas na função acessar_conta(cpf, contas, usuarios)

def verificar_extrato(contas, /, * numero_da_conta):

    saques = contas[numero_da_conta]['saques']
    depositos = contas[numero_da_conta]['depósitos']
    saldo = contas[numero_da_conta]['saldo']

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


def sacar(*, numero_da_conta, contas):
    print()
    print(mensagem_sacar)

    quantidade_saques = contas[numero_da_conta]['quantidade de saques']
    saldo = contas[numero_da_conta]['saldo']

    saque = float(input(mensagem_valor_saque))
    if saque <= VALOR_LIMITE_POR_SAQUE and quantidade_saques < LIMITE_DE_SAQUES and (saldo-saque) >= 0 and saque > 0:
        print(mensagem_saque_valido)
        return saque
    else:
        print(mensagem_saque_invalido)
        return False

# funções utilizadas na função opcoes_menu_conta(numero_de_contas_criadas, cpf, contas, usuarios)


def criar_conta(numero_de_contas_criadas, cpf, contas, usuarios):
    numero_de_contas_criadas += 1

    usuario = usuarios[cpf]['nome']

    contas[numero_de_contas_criadas] = {}
    contas[numero_de_contas_criadas]['numero'] = numero_de_contas_criadas
    contas[numero_de_contas_criadas]['agencia'] = AGENCIA
    contas[numero_de_contas_criadas]['usuario'] = usuario
    contas[numero_de_contas_criadas]['saldo'] = 0
    contas[numero_de_contas_criadas]['quantidade de saques'] = 0
    contas[numero_de_contas_criadas]['quantidade de depósitos'] = 0
    contas[numero_de_contas_criadas]['saques'] = []
    contas[numero_de_contas_criadas]['depósitos'] = []

    usuarios[cpf]['contas'][numero_de_contas_criadas] = contas[numero_de_contas_criadas]

    print(mensagem_conta_criada)

    return numero_de_contas_criadas


def listar_contas(usuarios, cpf):
    contas = usuarios[cpf]['contas']
    saida_de_texto = ["Numero da conta: ",
                      "Agência: ",
                      "Titular: ",
                      "Saldo: R$"]

    print(mensagem_lista_de_contas_usuario)
    print()

    for valor in contas.values():
        valores = valor.values()
        for i, msg in zip(valores, saida_de_texto):
            print(msg, end="")
            print(i)
        print()


def acessar_conta(cpf, contas, usuarios):
    acesso_a_conta = False

    while (acesso_a_conta == False):
        numero_da_conta = int(input(mensagem_numero_da_conta))
        if numero_da_conta in usuarios[cpf]['contas']:
            acesso_a_conta = True
        elif numero_da_conta == -1:
            return
        else:
            print(mensagem_conta_nao_existe)

    opcao = int(input(menu_operaçoes))

    while (opcao != 4):
        if opcao == 1:
            verificar_extrato(contas, numero_da_conta=numero_da_conta)
        elif opcao == 2:
            valor_depositado = depositar()
            if valor_depositado != False:
                contas[numero_da_conta]['depósitos'].append(valor_depositado)
                contas[numero_da_conta]['saldo'] += valor_depositado
                contas[numero_da_conta]['quantidade de depósitos'] += 1
                usuarios[cpf]['contas'][numero_da_conta] = contas[numero_da_conta]
        elif opcao == 3:
            valor_sacado = sacar(
                numero_da_conta=numero_da_conta, contas=contas)
            if valor_sacado != False:
                contas[numero_da_conta]['saques'].append(valor_sacado)
                contas[numero_da_conta]['saldo'] -= valor_sacado
                contas[numero_da_conta]['quantidade de saques'] += 1
                usuarios[cpf]['contas'][numero_da_conta] = contas[numero_da_conta]
        else:
            print(mensagem_opcao_invalida)
        opcao = int(input(menu_operaçoes))

# Funções que serão executadas dentro da função main()


def cadastrar_usuario(usuarios):
    print("Cadastrar Usuario")

    cpf = int(input(mensagem_dados_cpf))

    if verificar_cpf_na_lista_de_usuarios(usuarios=usuarios, cpf_usuario=cpf) == False:
        return usuarios, False

    usuarios[cpf] = {}
    usuarios[cpf]['nome'] = input(mensagem_dados_nome)
    usuarios[cpf]['data_de_nascimento'] = input(
        mensagem_dados_data_de_nascimento)

    usuarios[cpf]['endereco'] = {}
    print(mensagem_dados_endereco)
    usuarios[cpf]['endereco']['logradouro'] = input(mensagem_dados_logradouro)
    usuarios[cpf]['endereco']['numero'] = input(mensagem_dados_numero)
    usuarios[cpf]['endereco']['bairro'] = input(mensagem_dados_bairro)
    usuarios[cpf]['endereco']['cidade'] = input(mensagem_dados_cidade)
    usuarios[cpf]['endereco']['estado'] = input(mensagem_dados_estado)

    usuarios[cpf]['contas'] = {}

    print(mensagem_cadastro_sucesso)
    return usuarios, cpf


def verificar_cpf_na_lista_de_usuarios(usuarios, cpf_usuario):
    if cpf_usuario in usuarios:
        print(mensagem_cpf_cadastrado)
        return False


def login_com_cpf(usuarios):
    print(mensagem_login_usuario)
    print()
    usuario_cadastrado_na_lista = False
    while (usuario_cadastrado_na_lista == False):
        cpf_usuario = int(input(mensagem_dados_cpf))
        print()
        if cpf_usuario in usuarios:
            usuario_cadastrado_na_lista = True
            return cpf_usuario
        elif cpf_usuario == -1:
            print(mensagem_volta_para_o_menu)
            return False
        else:
            print(mensagem_cpf_ja_possui_cadastro)


def opcoes_menu_conta(numero_de_contas_criadas, cpf, contas, usuarios):
    opcao = int(input(menu_conta))
    while (opcao != 4):
        if opcao == 1:
            numero_de_contas_criadas = criar_conta(
                numero_de_contas_criadas, cpf, contas, usuarios)
        elif opcao == 2:
            if 'contas' in usuarios[cpf]:
                listar_contas(usuarios, cpf)
            else:
                print(mensagem_nao_possui_contas)
        elif opcao == 3:
            if 'contas' in usuarios[cpf]:
                acessar_conta(cpf, contas, usuarios)
            else:
                print(mensagem_nao_possui_contas)
        else:
            print(mensagem_opcao_invalida)

        opcao = int(input(menu_conta))

    print(mensagem_voltando_para_o_menu)


def visualizar_dados_do_usuario(**usuario):

    print(mensagem_visualizacao_dados_usuario)
    print("""
        Nome: {usuario[nome]} \t Data de nascimento: {usuario[data_de_nascimento]}
        Endereço: {usuario[endereco][logradouro]} \t\tNúmero: {usuario[endereco][numero]}
        Bairro: {usuario[endereco][bairro]} \tCidade: {usuario[endereco][cidade]} \Estado: {usuario[endereco][estado]}
          """.format(**usuario))


# Função main() que executa todo o sistema bancário


def main():
    print()
    print(mensagem_inicial)
    numero_de_contas_criadas = 0
    usuarios = {}
    contas = {}

    opcao_usuario = int(input(menu_principal))

    while (opcao_usuario != 3):

        while (opcao_usuario > 3 or opcao_usuario < 1):
            print(mensagem_opcao_invalida, end="")
            opcao_usuario = int(input(menu_principal))
        if opcao_usuario == 1:
            usuarios, cpf_usuario = cadastrar_usuario(usuarios)
            if cpf_usuario != False:
                opcoes_menu_conta(numero_de_contas_criadas,
                                  cpf_usuario, contas, usuarios)
        elif opcao_usuario == 2:
            cpf_usuario = login_com_cpf(usuarios)
            if cpf_usuario != False:
                visualizar_dados_do_usuario(usuario=usuarios[cpf_usuario])
                opcoes_menu_conta(numero_de_contas_criadas,
                                  cpf_usuario, contas, usuarios)
        elif opcao_usuario == 3:
            print(mensagem_final)
            return

        opcao_usuario = int(input(menu_principal))


main()
