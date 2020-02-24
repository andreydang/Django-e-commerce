from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Product


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'products/list.html'

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView).get_context_data(*args, **kwargs)
    #     return context


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "products/list.html", context)


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'products/detail.html'


def product_detail_view(request, pk=None):
    qs = Product.objects.filter(id=pk)
    if qs.exists() and qs.count() == 1:
        instance = qs.first()
    else:
        raise Http404("Product doesnt exist")

    # instance = Product.objects.get(pk=pk)
    # instance = get_object_or_404(Product, pk=pk)
    context = {
        'object': instance
    }
    return render(request, "products/detail.html", context)
