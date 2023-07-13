from django.shortcuts import render,redirect


def product_list(request):

    products = {"dairy": ["milk", "yogurt", "cheese", "butter"],
                "beverages": ["soda", "juice"],
                "vegetables": ["ginger", "lettuce", "spinach"],
                "fruits": ["bananas", "apples", "grapes"]}

    return render(request, "products_list.html", products)
