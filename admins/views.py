from django.shortcuts import render
from .models import Products
from PIL import Image


# Create your views here.
def alogin(request):
    if request.method == 'POST':
        try:
            email = request.POST.get('email')
            paw = request.POST.get('paw')
            if email == 'admin@gmail.com' and paw == 'admin':
                return render(request, 'a_home.html')
            else:
                return render(request, 'a_login.html')
        except Exception as e:
            print("Exception is :", e)
            return render(request, 'a_login.html')
    else:
        return render(request, 'a_login.html')


def addproduct(request):
    if request.method == 'POST':
        try:
            pname = request.POST.get('pname')
            pcat = request.POST.get('pcat')
            pcost = request.POST.get('pcost')
            pquality = request.POST.get('pquality')
            pdec = request.POST.get('pdec')
            pimage = request.FILES['pimage']
            data = Products(
                pname=pname,
                pcat=pcat,
                pcost=pcost,
                pquality=pquality,
                pdec=pdec,
                pimage=pimage,

            )
            data.save()
            return render(request, 'a_viewproducts.html')
        except Exception as e:
            print("Exception is:", e)
            return render(request, 'a_addproduct.html')


    else:
        return render(request, 'a_addproduct.html')


def products(request):
    data=Products.objects.all()
    return render(request, 'a_viewproducts.html',{'data':data})


def ahome(request):
    return render(request,'a_home.html')