from django.shortcuts import render, redirect
from products import models, forms

def set_netdevice(request):
    if request.method == 'POST':
        form = forms.AddNetworkDevice(request.POST)
        if form.is_valid():
            cleaned = form.cleaned_data
            brand = cleaned['brand']
            product_model = cleaned['model']
            product_type = cleaned['product_type']
            price = cleaned['price']
            description = cleaned['description']
            object = models.NetworkDevice(brand=brand, product_model=product_model, product_type=product_type, price=price, description=description)
            object.save()
            id = models.GlobalSearch(name=object.__str__(), id=object)
            id.save()
            return redirect('homepage')
        else:
            return render(request, 'sites/network.html', {'form':form})
    else:
        form = forms.AddNetworkDevice()
    return render(request, 'sites/network.html', {'form':form})

def set_iotdevice(request):
    if request.method == 'POST':
        form = forms.AddIoTDevice(request.POST)
        if form.is_valid():
            cleaned = form.cleaned_data
            brand = cleaned['brand']
            product_model = cleaned['model']
            product_type = cleaned['product_type']
            price = cleaned['price']
            description = cleaned['description']
            object = models.IoTDevice(brand=brand, product_model=product_model, product_type=product_type, price=price, description=description)
            object.save()
            id = models.GlobalSearch(name=object.__str__(), id=object)
            id.save()
            return redirect('homepage')
    else:
        form = forms.AddIoTDevice()
    return render(request, 'sites/iot.html', {'form':form})

def set_hwcomp(request):
    if request.method == 'POST':
        form = forms.AddHardwareComponent(request.POST)
        if form.is_valid():
            cleaned = form.cleaned_data
            brand = cleaned['brand']
            product_model = cleaned['model']
            product_type = cleaned['product_type']
            price = cleaned['price']
            description = cleaned['description']
            object = models.HardwareComponent(brand=brand, product_model=product_model, product_type=product_type, price=price, description=description)
            object.save()
            id = models.GlobalSearch(name=object.__str__(), id=object)
            id.save()
            return redirect('homepage')
    else:
        form = forms.AddHardwareComponent()
    return render(request, 'sites/hardware.html', {'form':form})

def search(request):
    form = forms.Search(request.GET)
    # if request.GET == {}:
    #     return render(request,'sites/search.html', {'form':form})
    
    if form.is_valid():
        if form.cleaned_data.get('input'):
            find = form.cleaned_data.get('input')
            if models.GlobalSearch.objects.filter(name__icontains = find):
                results = models.GlobalSearch.objects.filter(name__icontains = find)
                return render(request,'sites/search.html', {'form':form,'results':results})
            else:
                return render(request,'sites/search.html', {'form':form,'results':False})
        else:
            return render(request,'sites/search.html', {'form':form})


def get_database(request):
    network = models.NetworkDevice.objects.all()
    iot = models.IoTDevice.objects.all()
    hw = models.HardwareComponent.objects.all()
    return render(request, 'sites/database.html',{'network':network ,'iot':iot ,'hw':hw})

def delete(request, object_id):
    to_delete = models.Products.objects.get(id=object_id)
    to_delete.delete()
    return redirect('database')

def update(request, object_id):
    modify = models.Products.objects.get(id=object_id)
    form = forms.UpdateDevice(initial={'brand':modify.brand, 'model':modify.product_model, 'product_type':modify.product_type, 'price':modify.price, 'description':modify.description})
    if request.method == "POST":
        form = forms.UpdateDevice(request.POST)
        if form.is_valid():
            cleaned = form.cleaned_data
            modify.brand = cleaned['brand']
            modify.product_model = cleaned['model']
            modify.product_type = cleaned['product_type']
            modify.price = cleaned['price']
            modify.description = cleaned['description']
            modify.save()
            return redirect('database')
    return render(request, 'sites/update.html',{'form':form})