from django.shortcuts import render,redirect
from .models import Register,Purchase
from admins.models import Products
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')


def reg(request):
    if request.method=='POST':
        try:
            cname = request.POST.get('cname')
            email = request.POST.get('email')
            paw = request.POST.get('paw')
            mno = request.POST.get('mno')
            addr = request.POST.get('addr')
            pin = request.POST.get('pin')
            data = Register(
                cname=cname,
                cemail=email,
                paw=paw,
                mno=mno,
                addr=addr,
                pincode=pin,)
            data.save()
            return render(request,'Login.html')
        except Exception as e:
            print("Exception is:",e)
    else:
        return render(request,'Register.html')


def login(request):
    if request.method=='POST':
        try:
            email=request.POST.get('email')
            paw=request.POST.get('paw')
            data=Register.objects.get(cemail=email,paw=paw)
            print(data)
            request.session['userid'] = data.cemail #This is for making session
            print(request.session['userid'])
            return render(request,'U_home.html')
        except Exception as e:
            print("Exception is :",e)
            return render(request,'Login.html')
    else:
        return render(request,'Login.html')


def profile(request):
    try:
        uid = request.session['userid']
        print(uid)
        data=Register.objects.get(cemail=uid)
        cid=data.id
        return render(request,'U_profile.html',{'Profile':[data]})
    except Exception as e:
        print("Exception is:",e)
        return render(request,'U_home.html')


def products(request):
    data=Products.objects.all()
    return render(request,'U_product.html',{'Products':data})


def purchase(request):
    uid=request.session['userid']
    cdata=Register.objects.get(cemail=uid)
    cid=cdata.id
    data=Purchase.objects.filter(cid_id=cid)
    return render(request,'U_purchase.html',{'data':data ,'data2': cdata})


def logout(request):
    return render(request,'home.html')


def buy_product(request,id):
    if request.method == 'POST':
        uid = request.session['userid']
        cid=Register.objects.get(cemail=uid)
        id1=cid.id
        pid=request.POST.get('id')
        print("Pid is:",pid)
        product = Products.objects.get(id=id)
        data=Purchase(
            pname=product.pname,
            pcost=product.pcost,
            pquality=product.pquality,
            pdec=product.pdec,
            cid_id=id1,
            pid_id=id,
        )
        data.save()

        messages.success(request, 'Product purchased successfully.')
        return render(request, 'U_product.html')
    else:
        messages.error(request, 'Not Purchased.')
        return redirect('products')


def home(request):
    return render(request,'home.html')