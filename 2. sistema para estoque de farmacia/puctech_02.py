# Estoque inicial

estoque = {}    #dicionario (acessa por nome)

#funções: (crud)
def adicionar_medicamento(nome, quantidade):
    if nome in estoque:
        print(f"[!] {nome} ja esta registrado")

    else:
        estoque[nome]=quantidade
        print(f"[+] medicamento {nome} foi adicionado com {estoque[nome]} unidades")
        print("registro realizado")


def atualizar_estoque(nome, nova_qtd):
    pass

def listar_estoque():
    if not estoque:
        print("[!] estoque vazio")
        return
    print("--inventario--")
    for nome,quantidade in estoque.items():
        print(f"{nome}: {quantidade} unidades")
        

def deletar_medicamento(nome):
    pass

def processar_pedidos(pedidos):
    pass

#def exibir_resumo():
 #   pass


#teste do programa
while(True):
    print("\n")
    print('|--estoque--|')
    print('[1]registrar')
    print("[2]entrada")
    print("[3]listar")
    
    comando=int(input("Digite a função desejada: "))

    if(comando==1):
        print("--registro--")
        nome=input("nome: ")
        quantidade=int(input("quantidade: "))
        adicionar_medicamento(nome, quantidade)
        
    
    if(comando==3):
        listar_estoque()

    if(comando==0):
        print("exit")
        break

    