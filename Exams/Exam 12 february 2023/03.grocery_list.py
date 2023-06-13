def shop_from_grocery_list(budget, products, *args):

    bought_products = []

    for product, price in args:
        if product not in products:
            continue
        if product in bought_products:
            continue
        if price <= budget:
            budget -= price
            bought_products.append(product)
            products.remove(product)
        else:
            break

    if products:
        return f"You did not buy all the products. Missing products: {', '.join(products)}."
    else:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))
