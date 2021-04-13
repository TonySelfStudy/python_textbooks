from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm, RawProductForm


def product_delete_view(request, product_id):
    print(f'in product_delete_view()')
    obj = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        obj.delete()
        return redirect('/')
    context = {
        "object": obj,
        "product_id": product_id
    }
    return render(request, "products/product_delete.html", context)


def dynamic_lookup_view(request, product_id):
    print(f'in dynamic_lookup_view()')

    obj = get_object_or_404(Product, id=product_id)
    context = {
        "object": obj
    }
    return render(request, "products/product_detail.html", context)


# Create your views here.
def product_detail_view(request):
    obj = Product.objects.get(id=2)

    context = {
        'object': obj
    }
    return render(request, "products/product_detail.html", context)


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)


# def product_create_view(request):
#     print(f'{request=}')
#     print(f'{request.method=}')
#     print(f'{request.GET=}')
#     print(f'{request.POST=}')
#     context = {
#     }
#     return render(request, "products/product_create.html", context)
#
# def product_create_view(request):
#     print(f'{request=}')
#     print(f'{request.method=}')
#     print(f'{request.GET=}')
#     print(f'{request.POST=}')
#
#     if request.method == "GET":
#         my_form = RawProductForm()
#     if request.method == "POST":
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             # now you have good data
#             print(f'\n{my_form.cleaned_data=}')
#             Product.objects.create(**my_form.cleaned_data)
#         else:
#             print(f'\n{my_form.errors=}')
#
#     context = {"form": my_form
#                }
#     return render(request, "products/product_create.html", context)


def product_post(request):
    print(f'{request=}')
    print(f'{request.method=}')
    print(f'{request.GET=}')
    print(f'{request.POST=}')

    my_obj = vars(request).copy()
    print(my_obj)
    context = {"my_obj": my_obj}
    return render(request, "products/product_post.html", context)

