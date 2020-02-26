from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import MultipleObjectsReturned
# Create your views here.
from .models import Product


class ProductFeatureListView(ListView):
    template_name = 'products/list.html'

    def get_queryset(self):
        request = self.request
        return Product.objects.all().featured()


class ProductFeatureDetailView(DetailView):
    template_name = 'products/featured-detail.html'

    def get_queryset(self):
        request = self.request
        return Product.objects.all().featured()


class ProductListView(ListView):
    template_name = 'products/list.html'

    def get_queryset(self):
        request = self.request
        return Product.objects.all()
    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView).get_context_data(*args, **kwargs)
    #     return context


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "products/list.html", context)


class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = 'products/detail.html'

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        #instance = get_object_or_404(slug=slug, active=True)
        try:
            instance = Product.objects.get(slug=slug, active=True)
        except ObjectDoesNotExist:
            raise Http404("Not found")
        except MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404("Hmmm")
        return instance


class ProductDetailView(DetailView):
    template_name = 'products/detail.html'
    queryset = Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)  # .first()
        if instance is None:
            raise Http404("Product doesnt exist")
        return instance

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     pk = self.kwargs.get('pk')
    #     return Product.objects.filter(pk=pk)


def product_detail_view(request, pk=None):
    instance = Product.objects.get_by_id(pk)  # .first()
    if instance is None:
        raise Http404("Product doesnt exist")

    # qs = Product.objects.filter(id=pk)
    # if qs.exists() and qs.count() == 1:
    #     instance = qs.first()
    #     print(instance)
    # else:
    #     raise Http404("Product doesnt exist")

    # instance = Product.objects.get(pk=pk)
    # instance = get_object_or_404(Product, pk=pk)
    context = {
        'object': instance
    }
    return render(request, "products/detail.html", context)
