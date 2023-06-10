"""ECom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user import views as v
from admins import views as v1
from django.conf import settings
from django.conf.urls.static import static
app_name = 'user'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v.index, name='index'),#
    path('home', v.home, name='home'),
    path('reg/', v.reg, name='reg'),#
    path('login/', v.login, name='login'),
    path('profile/', v.profile, name='profile'),
    path('product/<int:id>/', v.products, name='products'),#
    path('product/', v.products, name='products'),
    path('buyproduct/<int:id>/buy/', v.buy_product, name='buy_product'),
    path('purchase/', v.purchase, name='purchase'),
    path('logout/', v.logout, name='logout'),

    path('alogin/', v1.alogin, name='alogin'),
    path('ahome/', v1.ahome, name='ahome'),
    path('addproduct/', v1.addproduct, name='addproduct'),
    path('aviewproducts/', v1.products, name='viewproducts'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
