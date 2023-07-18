from django.shortcuts import render,redirect
from .models import OrderList
from django.contrib import messages
from groceries_app import views as grocires


def product_list(request):

    products = {"dairy": ["milk", "yogurt", "cheese", "butter"],
                "beverages": ["soda", "juice"],
                "vegetables": ["ginger", "lettuce", "spinach"],
                "fruits": ["bananas", "apples", "grapes"]}

    return render(request, "products_list.html", products)


def order(request):
    global usrnme
    if request.method =="POST":
        prod_list = request.POST.getlist('products')
        prod_str = ",".join(prod_list)
        order_data = OrderList(wholeList=prod_str,username=grocires.usrnme)
        order_data.save()
        messages.success(request,"order created successfully"+prod_str)
        return redirect("loggedin")
    else:
        return render(request,"products_list.html")

