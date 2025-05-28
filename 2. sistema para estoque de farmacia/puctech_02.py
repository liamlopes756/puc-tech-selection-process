# Estoque inicial

estoque = {}    #dicionario (acessa por nome)

#funções: (crud)
def adicionar_medicamento(nome, quantidade):
    if nome in estoque:
        print(f"[!] {nome} ja esta registrado")

    else:
        estoque[nome]=quantidade
        print(f"[+] medicamento {nome} foi adicionado com {estoque[nome]} unidades")


def atualizar_estoque(nome, nova_qtd):
    pass

def listar_estoque():
    if not estoque:
        print("[!] estoque vazio")
        return
    #for
        

def deletar_medicamento(nome):
    pass

def processar_pedidos(pedidos):
    pass

def exibir_resumo():
    pass