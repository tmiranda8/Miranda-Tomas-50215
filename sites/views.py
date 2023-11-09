from django.shortcuts import render, redirect
from sites import models, forms

def homepage(request):
	return render(request, 'index.html',{})

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
            object = models.NetworkDevices(brand=brand, product_model=product_model, product_type=product_type, price=price, description=description)
            object.save()
            id = models.GlobalSearch(identifier=object.__str__())
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
            object = models.IoTDevices(brand=brand, product_model=product_model, product_type=product_type, price=price, description=description)
            object.save()
            id = models.GlobalSearch(identifier=object.__str__())
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
            object = models.HardwareComponents(brand=brand, product_model=product_model, product_type=product_type, price=price, description=description)
            object.save()
            id = models.GlobalSearch(identifier=object.__str__())
            id.save()
            return redirect('homepage')
    else:
        form = forms.AddHardwareComponent()
    return render(request, 'sites/hardware.html', {'form':form})

def get_device(request):
    find = request.GET.get('word')
    if find:
        results = models.GlobalSearch.objects.filter(identifier__icontains = find)
    else:
        results = ''
    return render(request,'sites/search.html', {'results':results})
    # form = forms.Search()
    # form = forms.Search(request.GET)
    # if form.is_valid():
    #     find = form.cleaned_data.get('word')
    #     find_in = request.GET.get('device')
    #     category = request.GET.get('category')
    #     if find_in == 'network':
    #         if category == 'brand':
    #             results = models.NetworkDevices.objects.filter(brand__icontains = find)
    #         elif category == 'model':
    #             results = models.NetworkDevices.objects.filter(product_model__icontains = find)
    #         elif category == 'type':
    #             results = models.NetworkDevices.objects.filter(product_type__icontains = find)
    #         else:
    #             results = models.NetworkDevices.objects.all()
    #         return render(request,'sites/search.html', {'result':results})
    #     elif find_in == 'iot':
    #         if category == 'brand':
    #             results = models.IoTDevices.objects.filter(brand__icontains = find)
    #         elif category == 'model':
    #             results = models.IoTDevices.objects.filter(product_model__icontains = find)
    #         elif category == 'type':
    #             results = models.IoTDevices.objects.filter(product_type__icontains = find)
    #         else:
    #             results = models.IoTDevices.objects.all()
    #         return render(request,'sites/search.html', {'result':results})
    #     elif find_in == 'hw':
    #         if category == 'brand':
    #             results = models.HardwareComponents.objects.filter(brand__icontains = find)
    #         elif category == 'model':
    #             results = models.HardwareComponents.objects.filter(product_model__icontains = find)
    #         elif category == 'type':
    #             results = models.HardwareComponents.objects.filter(product_type__icontains = find)
    #         else:
    #             results = models.HardwareComponents.objects.all()
    #         return render(request,'sites/search.html', {'results':results})
    # else:
    #     return render(request,'sites/search.html', {'form':form})

def get_database(request):
    network = models.NetworkDevices.objects.all()
    iot = models.IoTDevices.objects.all()
    hw = models.HardwareComponents.objects.all()
    return render(request, 'sites/database.html',{'network':network ,'iot':iot ,'hw':hw})