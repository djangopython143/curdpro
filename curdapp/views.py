from django.shortcuts import render
from .models import ProductData
from django.http.response import HttpResponse

def home(request):
    return render(request,'curd.html')
def insert_view(request):
    if request.method=='POST':
            data=ProductData(product_id = request.POST.get('product_id'),
            product_name = request.POST.get('product_name'),
            product_cost = request.POST.get('product_cost'),
            product_class = request.POST.get('product_class'),
            no_of_products = request.POST.get('no_of_products'),
            manfacture_date=request.POST.get('manfacture_date'),
            expiry_date = request.POST.get('expiry_date'),
            customer_name = request.POST.get('customer_name'),
            mobile = request.POST.get('mobile'),
            email = request.POST.get('email'))
            # data=ProductData(product_id=product_id,product_name=product_name,
            #             product_cost=product_cost,product_class=product_class,
            #             no_of_products=no_of_products,manfacture_date=manfacture_date,
            #             expiry_date=expiry_date,customer_name=customer_name,
            #             mobile=mobile,email=email)
            data.save()
            return HttpResponse('201-ok')
    else:
        return render(request,'insert.html')
def retrieve_view(request):
    data=ProductData.objects.all()
    return render(request,'retrieve.html',{'data':data})

def put(request):
    if request.method=='POST':
        prid=request.POST.get('pid')
        pcost=request.POST.get('cost')
        proid=ProductData.objects.filter(product_id=prid)
        if not proid:
            return HttpResponse('Product Not available')
        else:
            proid.update(product_cost=pcost)
            return HttpResponse('Updated Successfully')
    else:
        return render(request,'update.html')
def delete(request):
    if request.method=='POST':
        prid=request.POST.get('pid')
        proid=ProductData.objects.filter(product_id=prid)
        if not proid:
            return HttpResponse('Product Not available')
        else:
            proid.delete()
            return HttpResponse('Deleted Successfully')
    else:
        return render(request,'delete.html')