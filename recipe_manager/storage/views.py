from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .models import StorageItem

# Create your views here.
class StorageView(ListView):
    model = StorageItem
    template_name = "storage.html"


def DeleteItemView(request, id):
    item = StorageItem.objects.get(id=id)
    item.delete()
    return redirect('storage')

def AddItemView(request):
    if request.method == 'POST':
        item = StorageItem.objects.create(
            name = request.POST.get('name'),
            quantity = request.POST.get('quantity'),
            price = request.POST.get('price'),
        )
        item.save()
    return render(request, 'add_item.html')

def EditItemView(request, id):
    item = get_object_or_404(StorageItem, id=id)

    if request.method == "POST":
        name = request.POST.get('name')
        if request.POST.get('quantity'):
            quantity = float(request.POST.get('quantity'))
            item.quantity = quantity

        if request.POST.get('price'):
            paid_price = float(request.POST.get('price'))
            item.price = paid_price

        item.name = name
        item.save()        
        return redirect('storage')