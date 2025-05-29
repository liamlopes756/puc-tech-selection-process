
# Estoque inicial
estoque = {}    #dicionario (acessa por nome)

#funções: (crud)
def adicionar_medicamento(nome, quantidade):#create
    if nome in estoque:
        print(f"[!] {nome} ja esta registrado")

    else:
        estoque[nome]=quantidade
        print(f"[+] medicamento {nome} foi adicionado com {estoque[nome]} unidades")
        print("registro realizado")


def atualizar_estoque(nome, nova_qtd):#update
   
    if(nome in estoque):
       estoque[nome] +=nova_qtd
       print(f"{nome} atualizado: {estoque[nome]} unidades")
    else:
        print("[!] Nao cadastrado")
    

def listar_estoque():#read
    if not estoque:
        print("[!] estoque vazio")
        return
    print("--inventario--")
    for nome,quantidade in estoque.items():
        print(f"{nome}: {quantidade} unidades")
        

def deletar_medicamento(nome):#delete
    if nome in estoque:
        del estoque[nome]
        print(f"[!]{nome} deletado.")

def processar_pedidos(nome,qtd_pedido):#update

    if nome not in estoque:
        print(f"[X] '{nome}' não está no estoque.")
    elif estoque[nome] == 0:
        print(f"[X] '{nome}' está esgotado.")
    elif estoque[nome] < qtd_pedido:
        print(f"[!] Estoque insuficiente de '{nome}'. Apenas {estoque[nome]} disponíveis.")
    else:
        estoque[nome] -= qtd_pedido
        print(f"[✓] Pedido de {qtd_pedido}x '{nome}' processado. Restam {estoque[nome]} unidades.")



#teste do programa
while(True):
    print("\n")
    print('|--Sistema de Estoque--|')
    print('[1]Registrar')
    print("[2]Entrada")
    print("[3]Relatorio")
    print("[4]Processamento de Pedidos")
    print("[5]Deletar produto")

    print("[0]Sair")
    
    comando=int(input("Digite a função desejada: "))
    print("\n")

    if(comando==1):
        print("--registro--")
        nome=input("nome: ")
        quantidade=int(input("quantidade: "))
        adicionar_medicamento(nome, quantidade)

    if comando==2:
         print("--entrada de medicamentos--")
         nome=input("nome: ") #sempre string
         nova_qtd=int(input("quantidade: "))
         atualizar_estoque(nome, nova_qtd)

        
    
    if(comando==3):
        listar_estoque()

    if(comando==4):
        print("--Processamento de pedidos--")
        nome=input("Medicamento: ")
        qtd_pedido=int(input("Quantidade pedida:"))
        processar_pedidos(nome,qtd_pedido)



    if(comando==5):
        print("--Deletar Produtos--")
        nome=input("Medicamento a ser deletado:  ")
        deletar_medicamento(nome)


    if(comando==0):
        print("exit")
        break

    