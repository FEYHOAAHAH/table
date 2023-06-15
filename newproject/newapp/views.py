from django.shortcuts import render
from .models import Products, Orders, Users, Mouses, Keyboards, Headphones, Gamepads, Notebooks


# Create your views here.

def show_data(request):
    products = Products.objects.all()
    orders = Orders.objects.all()
    users = Users.objects.all()
    mouses = Mouses.objects.all()
    keyboards = Keyboards.objects.all()
    headphones = Headphones.objects.all()
    gamepads = Gamepads.objects.all()
    notebooks = Notebooks.objects.all()

    return render(request, 'index.html', {'products': products, 'orders': orders, 'users': users,
                                          'mouses': mouses, 'keyboards': keyboards,
                                          'headphones':  headphones, 'gamepads': gamepads, 'notebooks': notebooks})



