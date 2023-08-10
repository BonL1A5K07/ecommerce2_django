from django.shortcuts import render,get_object_or_404,redirect
from .models import Item,Category

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import NewItemForm,EditItemForm
# Create your views here.

def items(request):
    #input name=query
    query = request.GET.get('query','')
    category_id = request.GET.get('category',0)
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)
    
    if category_id:
        items = items.filter(category_id=category_id)
    # tìm kiếm ở dưới name serch và description trong serch có chứa ký tự giống db thì hiện
    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))
    
    return render(request,'item/items.html',{
        'items':items,
        'query':query,
        'categories':categories,
        'category_id':int(category_id),
    })

def detail(request,pk):
    #item = Item.objects.get(pk=pk) 
    #pk(1) lay tu primary key db pk(2) lay tu url
    item = get_object_or_404(Item, pk=pk)# báo lỗi nếu nó không tồn tại trong db (được sử dụng nhiều)
    #Lấy item có cùng thể loại và chưa bán hết (lấy 3 sản phẩm đầu(chưa bán hết), 
    # loại trừ sản phẩm mình đang xem(pk=pk) trong details)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    return render(request,'item/detail.html',{
        'item':item,
        'related_items':related_items,
    })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST,request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.create_by = request.user
            item.save()

            return redirect('item:detail',pk=item.id)
    else:
        form = NewItemForm()

    return render(request, 'item/form.html',{
        'form':form,
        'title':"New Item",
    })

@login_required
def edit(request,pk):
    item = get_object_or_404(Item, pk=pk, create_by=request.user)
    if request.method == 'POST':
        form = EditItemForm(request.POST,request.FILES, instance=item)
        if form.is_valid():
            form.save()

            return redirect('item:detail',pk=item.id)
    else:
        #instance=item được sử dụng để điền dữ liệu của đối tượng item vào Form EditItemForm
        form = EditItemForm(instance=item)

    return render(request, 'item/form.html',{
        'form':form,
        'title':"Edit Item",
    })

@login_required
def delete(request,pk):
    item = get_object_or_404(Item, pk=pk, create_by=request.user)
    item.delete()

    return redirect('dashboard:index')