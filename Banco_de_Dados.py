produtos = [
    [101, "Notebook", 3500.00],
    [102, "Smartphone", 1800.00],
    [103, "Teclado Mecânico", 250.00],
    [104, "Mouse Sem Fio", 120.00]
]
print("--- 1. Cadastrando um novo produto ---")
novo_produto = [105, "Monitor 24'", 950.00]
produtos.append(novo_produto)
print(f"Produto '{novo_produto[1]}' cadastrado com sucesso.\n")

print("--- 2. Lista Completa de Produtos ---")
for prod in produtos:
    print(f"ID: {prod[0]} | Produto: {prod[1]} | Preço: R$ {prod[2]:.2f}")
print()

print("--- 3. Alterando o preço de um produto ---")
id_alterar = 102
novo_preco = 1650.00

for prod in produtos:
    if prod[0] == id_alterar:
        prod[2] = novo_preco
        print(f"Preço do produto '{prod[1]}' atualizado para R$ {novo_preco:.2f}.\n")
        break

print("--- 4. Localizando um produto pelo ID ---")
id_procurado = 103
encontrado = False

for prod in produtos:
    if prod[0] == id_procurado:
        print(f"Produto Encontrado -> ID: {prod[0]} | Nome: {prod[1]} | Preço: R$ {prod[2]:.2f}\n")
        encontrado = True
        break

if not encontrado:
    print(f"Produto com ID {id_procurado} não foi encontrado.\n")

print("--- 5. Removendo um produto pelo ID ---")
id_remover = 104
removido = None

for indice, prod in enumerate(produtos):
    if prod[0] == id_remover:
        removido = produtos.pop(indice)
        print(f"Produto '{removido[1]}' (ID {id_remover}) removido com sucesso.\n")
        break

if not removido:
    print(f"Não foi possível remover: ID {id_remover} não encontrado.\n")

print("--- 6. Lista de Produtos Atualizada ---")
for prod in produtos:
    print(f"ID: {prod[0]} | Produto: {prod[1]} | Preço: R$ {prod[2]:.2f}")
