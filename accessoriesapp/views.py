from math import ceil

from django.shortcuts import render

# Create your views here.
from accessoriesapp.forms import prodform
from accessoriesapp.models import prodmodel


def accessoriesview(request):
    # allprods = []
    # catprods = prodmodel.objects.values('Eqipment', 'id')
    #
    # cats = {item['Eqipment'] for item in catprods}
    # for cat in cats:
    #     prod = prodmodel.objects.filter(Eqipment=cat)
    #     n = len(prod)
    #     nSlides = n//2 + ceil((n/2) - (n//2))
    #     allprods.append([prod, range(1, nSlides), nSlides])
    #
    # return render(request, 'accessoriespage.html', {'dispproduct': allprods})


    dispproduct = prodmodel.objects.all()
    return render(request, 'accessoriespage.html', {'dispproduct': dispproduct})


def addaccessoriesview(request):
    if request.method == 'POST':
        form = prodform(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            print('Form Saved')

    form = prodform()
    return render(request, 'addprodform.html', {'form': form})


