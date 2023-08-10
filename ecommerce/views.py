from django.shortcuts import render,redirect

from item.models import Category,Item

from .forms import SignUpForm




# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories=Category.objects.all()

    return render(request,'ecommerce/index.html',{
        'categories':categories,
        'items':items,
    })

def contact(request):
    return render(request,'ecommerce/contact.html')

def signup(request):
    #Kiểm tra user đã submit chưa
    if request.method == 'POST':
        #Dữ liệu được gửi từ method Post thông qua submit đổ vào form
        form = SignUpForm(request.POST)
        #Kiểm tra dữ liệu có hợp lệ không 
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        #Nếu ko phải là POST hiển thị form trống để ngta nhập
        form = SignUpForm()

    return render(request,'ecommerce/signup.html',{
        'form':form,
    })