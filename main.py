import json

def load_data(file_name):
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data(file_name, data):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)

restaurants_file = 'restaurants.txt'
cart_file = 'cart.txt'

restaurants = load_data(restaurants_file)
cart = load_data(cart_file)

def add_item_menu():
    restaurant_name = input("Digite o nome do restaurante: ").lower()
    item_name = input("Digite o nome do item: ").lower()
    for restaurant in restaurants:
        if restaurant["nome"].lower() == restaurant_name:
            for category in restaurant["cardapio"].values():
                for item in category:
                    if item["nome"].lower() == item_name:
                        cart.append(item)
                        save_data(cart_file, cart)
                        print("Item adicionado ao menu")
                        return
            print("Produto não encontrado")
            return
    print("Este restaurante não está no nosso sistema, Verifique nossa lista novamente")

def remove_item_menu():
    restaurant_name = input("Digite o nome do restaurante: ").lower()
    item_name = input("Digite o nome do item: ").lower()
    for restaurant in restaurants:
        if restaurant["nome"].lower() == restaurant_name:
            for category in restaurant["cardapio"].values():
                for item in category:
                    if item["nome"].lower() == item_name:
                        cart.remove(item)
                        save_data(cart_file, cart)
                        print("Produto removido")
                        return
            print("Produto não encontrado")
            return
    print("Este restaurante não está no nosso sistema, Verifique nossa lista novamente")

def search_item_menu():
    restaurant_name = input("Digite o nome do restaurante: ").lower()
    item_name = input("Digite o nome do item: ").lower()
    for restaurant in restaurants:
        if restaurant["nome"].lower() == restaurant_name:
            for category in restaurant["cardapio"].values():
                for item in category:
                    if item["nome"].lower() == item_name:
                        print("Produto encontrado")
                        return
            print("Produto não encontrado")
            return
    print("Este restaurante não está no nosso sistema, Verifique nossa lista novamente")

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
        for category_name, category_items in restaurant["cardapio"].items():
            print(f'\nCategoria: {category_name.capitalize()}')
            for item in category_items:
                print(f'''Nome: {item["nome"]} - Preço: R${item["valor"]:.2f}''')
        print("\n###################################################")

def add_item():
    for restaurant in restaurants:
        print(f'''
            Restaurante: {restaurant["nome"]}
            Taxa do garçom: {restaurant["garcomTax"]}%''')
        for category_name, category_items in restaurant["cardapio"].items():
            print(f'''
                  Categoria: {category_name.capitalize()}''')
            for item in category_items:
                item["valor"] += item["valor"] * restaurant["garcomTax"] / 100
                print(f'''Nome: {item["nome"]} - Preço: R${item["valor"]:.2f}''')

    restaurant_name = input("Digite o nome do restaurante: ").lower()
    for restaurant in restaurants:
        if restaurant["nome"].lower() == restaurant_name:
            item_name = input("Digite o nome do item: ").lower()
            for category in restaurant["cardapio"].values():
                for item in category:
                    if item["nome"].lower() == item_name:
                        cart.append(item)
                        save_data(cart_file, cart)
                        print("Foi adicionado ao carrinho")
                        return
            print("Não temos esse item no cardápio")
            return
    print("Este restaurante não está no nosso sistema, Verifique nossa lista novamente")

def remove_item():
    for item in cart:
        print(f'''Nome: {item["nome"]} - Preço: R${item["valor"]:.2f}''')
    item_name = input("Digite o nome do item: ").lower()
    for item in cart:
        if item["nome"].lower() == item_name:
            cart.remove(item)
            save_data(cart_file, cart)
            print(f"Você retirou {item['nome']} do carrinho")
            return
    print("Este item não está no carrinho")

def list_items():
    for item in cart:
        print(f'''Nome: {item["nome"]} - Preço: R${item["valor"]:.2f}''')

def finish_order():
    total = 0
    for item in cart:
        total += item["valor"]
    print(f"Total: R${total:.2f}")
    cart.clear()
    save_data(cart_file, cart)
    print("Pedido finalizado")

# Main loop
while True:
    print('''
      \nBem-vindo ao APP DE DELIVERY 🛒 🛒 🛒 🛒 (Selecione uma opção digitando apenas o número)
      1 - Colocar produto no carrinho
      2 - Tirar produto do carrinho
      3 - Buscar produtos no carrinho
      4 - Ver carrinho
      5 - Buscar item no cardápio
      6 - Listar todas as lojas e cardápios
      7 - Adicionar item ao cardápio
      8 - Remover item do cardápio
      9 - Finalizar PEDIDO
    ''')
    option = input("Digite a opção: ")
    if option == "1":
        add_item()
    elif option == "2":
        remove_item()
    elif option == "3":
        search_item_menu()
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
