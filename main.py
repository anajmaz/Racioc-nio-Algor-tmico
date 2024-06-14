restaurants = [
    {
        "nome": "kfc",
        "garcomTax": 5,
        "cardapio": {
            "principal": [
                {
                    "nome": "nhoque 4 queijos",
                    "valor": 10
                },
                {
                    "nome": "churrasco",
                    "valor": 5
                },
            ],
            "bebidas": [
                {
                    "nome": "Agua",
                    "valor": 1.50
                },
                {
                    "nome": "Agua Tônica",
                    "valor": 2.50
                },
                {
                    "nome": "Suco de Uva",
                    "valor": 3.50
                }
            ],
            "pratos": [
                {
                    "nome": "Batata",
                    "valor": 10
                },
                {
                    "nome": "Frango",
                    "valor": 14.99
                },
            ],
            "entradas": [
                {
                    "nome": "pao",
                    "valor": 2.50
                },
                {
                    "nome": "salgado",
                    "valor": 2.99
                },
            ],
            "sobremesas": [
                {
                    "nome": "sorvete de chocolate",
                    "valor": 5
                },
                {
                    "nome": "cookies",
                    "valor": 4.99
                },
            ]
        }
    },
]
cart = []

def add_item_menu():
    restaurant_name = input("Digite o nome do restaurante: ").lower()
    item_name = input("Digite o nome do item: ").lower()
    for restaurant in restaurants:
        if restaurant["nome"] == restaurant_name:
            for item in restaurant["cardapio"]:
                if item["nome"].lower() == item_name:
                    cart.append(item)
                    print("Item adicionado ao cardapio")
                    return
            print("Item não encontrado")
            return
    print("Restaurante não encontrado")

def remove_item_menu():
    restaurant_name = input("Digite o nome do restaurante: ").lower()
    item_name = input("Digite o nome do item: ").lower()
    for restaurant in restaurants:
        if restaurant["nome"].lower() == restaurant_name:
            for item in restaurant["cardapio"]:
                if item["nome"].lower() == item_name:
                    cart.remove(item)
                    print("Item removido com sucesso")
                    return
            print("Item não encontrado")
            return
    print("Restaurante não encontrado")

def search_item_menu():
    restaurant_name = input("Digite o nome do restaurante: ").lower()
    item_name = input("Digite o nome do item: ").lower()
    for restaurant in restaurants:
        if restaurant["nome"].lower() == restaurant_name:
            for item in restaurant["cardapio"]:
                if item["nome"].lower() == item_name:
                    print("Item encontrado")
                    return
            print("Item não encontrado")
            return
    print("Restaurante não encontrado")

def list_items_menu():
    for item in cart:
        print(f'''
            Nome: {item["nome"]} - Preço: R${item["valor"]:.2f}
        ''')

def list_restaurants():
    for restaurant in restaurants:
        print(f'''
            Restaurante: {restaurant["nome"]}
            Taxa do garçom: {restaurant["garcomTax"]}%
        ''')
        for item in restaurant["cardapio"]:
            print(f'''
                Nome: {item["nome"]} - Preço: R${item["valor"]:.2f}
            ''')
        print("\n")

def add_item():
    for restaurant in restaurants:
        print(f'''
            Restaurante: {restaurant["nome"]}
            Taxa do garçom: {restaurant["garcomTax"]}%
        ''')
        for category in restaurant["cardapio"]:
            print(f'''
                Categoria: {category.capitalize()}
            ''')
            for item in restaurant["cardapio"][category]:
                item["valor"] += item["valor"] * restaurant["garcomTax"] / 100
                print(f'''
                    Nome: {item["nome"]} - Preço: R${item["valor"]:.2f}
                ''')

    restaurant_name = input("Digite o nome do restaurante: ").lower()
    for restaurant in restaurants:
        if restaurant["nome"].lower() == restaurant_name:
            item_name = input("Digite o nome do item: ").lower()
            for category in restaurant["cardapio"]:
                for item in restaurant["cardapio"][category]:
                    if item["nome"].lower() == item_name:
                        cart.append(item)
                        print("Item adicionado ao carrinho")
                        return
            print("Item não encontrado")
            return
    print("Restaurante não encontrado")

def remove_item():
    for item in cart:
        print(f'''Nome: {item["nome"]} - Preço: R${item["valor"]:.2f}''')
        item_name = input("Digite o nome do item: ").lower()
        if item["nome"].lower() == item_name:
            cart.remove(item)
            print("Item removido com sucesso")
            return
    print("Item não encontrado")

def list_restaurants():
    for restaurant in restaurants:
        print(f'''
            🛒 Restaurante: {restaurant["nome"]} 🛒
            Taxa do garçom: {restaurant["garcomTax"]}%''')
        for category in restaurant["cardapio"]:
            print(f'\nCategoria: {category.capitalize()}')
            for item in restaurant["cardapio"][category]:
                print(f'''Nome: {item["nome"]} - Preço: R${item["valor"]}''')
        print("\n###################################################")

def list_items():
    for item in cart:
        print(f'''Nome: {item["nome"]} - Preço: R${item["valor"]:.2f}''')

def finish_order():
    total = 0
    for item in cart:
        total += item["valor"]
    print(f"Total: R${total:.2f}")
    cart.clear()
    print("Pedido finalizado")
        
while True:
    print('''
      \nBem-vindo ao APP DE DELIVERY 🛒 🛒 🛒 🛒 ( Selecione uma opcao digite apenas o numero e nomes exatos )
      1 - colocar produto no carrinho
      2 - tirar produto do carrinho
      3 - buscar produtos no carrinho
      4 - Ver carrinho
      5 - buscar item no cardapio
      6 - listar todas as lojas e cardapios
      7 - adicionar item ao cardapio
      8 - remover item do cardapio
      9 - finalizar PEDIDO
    ''')
    option = input("Digite a opção: ")
    if option == "1":
        add_item()
    elif option == "2":
        remove_item()
    elif option == "4":
        list_items()
    elif option == "5":
        search_item_menu()
    elif option == "6":
        list_restaurants()
    elif option == "7":
        add_item_menu()
    elif option == "8":
        remove_item_menu()
    elif option == "9":
        finish_order()
