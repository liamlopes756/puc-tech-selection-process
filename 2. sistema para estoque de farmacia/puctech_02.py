# Estoque inicial (pode ser vazio)
estoque = {}

# Função para adicionar novo medicamento
def adicionar_medicamento(nome, quantidade):
    if nome in estoque:
        print(f"[!] O medicamento '{nome}' já existe. Use a função de atualização.")
    else:
        estoque[nome] = quantidade
        print(f"[+] Medicamento '{nome}' adicionado com {quantidade} unidades.")

# Função para atualizar a quantidade (ex: reposição)
def atualizar_estoque(nome, nova_qtd):
    if nome in estoque:
        estoque[nome] += nova_qtd
        print(f"[~] Estoque de '{nome}' atualizado para {estoque[nome]} unidades.")
    else:
        print(f"[!] Medicamento '{nome}' não encontrado.")

# Função para listar o estoque atual
def listar_estoque():
    if not estoque:
        print("[i] Estoque vazio.")
        return
    print("\n📦 Estoque Atual:")
    for nome, qtd in estoque.items():
        status = ""
        if qtd == 0:
            status = " (ESGOTADO)"
        elif qtd <= 5:
            status = " (⚠️ CRÍTICO)"
        print(f"- {nome}: {qtd} unidades{status}")

# Função para deletar medicamento do estoque
def deletar_medicamento(nome):
    if nome in estoque:
        del estoque[nome]
        print(f"[-] Medicamento '{nome}' removido do estoque.")
    else:
        print(f"[!] Medicamento '{nome}' não encontrado.")

# Função para processar pedidos de clientes
def processar_pedidos(pedidos):
    print("\n🧾 Processando pedidos...")
    for nome, qtd_pedido in pedidos.items():
        if nome not in estoque:
            print(f"[X] '{nome}' não está no estoque.")
        elif estoque[nome] == 0:
            print(f"[X] '{nome}' está esgotado.")
        elif estoque[nome] < qtd_pedido:
            print(f"[!] Estoque insuficiente de '{nome}'. Apenas {estoque[nome]} disponíveis.")
        else:
            estoque[nome] -= qtd_pedido
            print(f"[✓] Pedido de {qtd_pedido}x '{nome}' processado. Restam {estoque[nome]} unidades.")

# Função para exibir o resumo final
def exibir_resumo():
    print("\n📊 Resumo Final do Estoque:")
    listar_estoque()

# =========================
# 🧪 Teste das funcionalidades
# =========================
adicionar_medicamento("Paracetamol", 10)
adicionar_medicamento("Dipirona", 3)
adicionar_medicamento("Ibuprofeno", 0)

listar_estoque()

atualizar_estoque("Dipirona", 5)
atualizar_estoque("Omeprazol", 2)

deletar_medicamento("Ibuprofeno")

listar_estoque()

# Simulando pedidos de clientes
pedidos_clientes = {
    "Paracetamol": 4,
    "Dipirona": 6,
    "Omeprazol": 1,   # não existe
    "Ibuprofeno": 1   # foi removido
}

processar_pedidos(pedidos_clientes)

# Exibindo resumo final
exibir_resumo()