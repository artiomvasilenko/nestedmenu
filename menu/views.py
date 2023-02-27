from django.shortcuts import render
from .models import Menu, Item

# Create your views here.
def main(request):
    menus = Menu.objects.all()
    return render(request, 'main.html', {'menus': menus})

def menu(request, id):
    menus = Menu.objects.all()
    items = Item.objects.filter(menu_id=id)

    return render(request, 'main.html', {'id': id, 'menus': menus, 'items': items})