from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.
from BuyProdApp.forms import BuyProductForm
from BuyProdApp.models import BuyProductModel

def ByeProdpage(request):
    if request.method == 'POST':
        form = BuyProductForm(request.POST)
        if form.is_valid():
            form.save()

    if request.user.is_authenticated:
        form = BuyProductForm()
        return render(request, 'ByeProdForm.html', {'form': form})
    else:
        messages.success(request, 'Please LogIn to Buy')
        return redirect('accessoriesview')

def UserPurchaedPrd(request):
    PurchasedProd = BuyProductModel.objects.all()
    return render(request, 'UserPurchasedProd.html', {'PurchasedProd': PurchasedProd})










