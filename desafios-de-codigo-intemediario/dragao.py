C = int(input())
for i in range(C):
    N = int(input())
    mensagem = "Inseto!" if N <= 8000 else "Mais de 8000!"
    print(mensagem)
