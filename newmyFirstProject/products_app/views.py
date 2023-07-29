from django.shortcuts import render,redirect
from .models import OrderList
from django.contrib import messages
from groceries_app import views as groc_view
from groceries_app import models as groc_model
from django.core.mail import send_mail
from django.conf import settings



def product_list(request):

    products = {"dairy": ["milk", "yogurt", "cheese", "butter"],
                "beverages": ["soda", "juice"],
                "vegetables": ["ginger", "lettuce", "spinach"],
                "fruits": ["bananas", "apples", "grapes"]}

    return render(request, "products_list.html", products)


def order(request):
    if request.method == 'POST':
        prod_list = request.POST.getlist('products')
        prod_str = ",".join(prod_list)
        order_data = OrderList(wholelist=prod_str, username=groc_view.usrnme)
        order_data.save()
        user_data = groc_model.RegisteredUser.objects.get(name=groc_view.usrnme)
        # recipientlist = [user_data.emailid, ]
        # send_mail(
        #     "Order from Loony Basket",
        #     "Hi, \n \n Below are the products that you have ordered from Loony Basket.\n\n {}".format(prod_str),
        #     settings.EMAIL_HOST_USER,
        #     recipientlist
        # )
        messages.success(request, "Order has been created successfully and a mail with the list of"
                                  " products has been sent to your registered email address")
        return render(request, "ordersuccess.html")

    else:
        return render(request, "product_list.html")


def hourscaluclator(request):


    return render(request, "products_list.html", products)