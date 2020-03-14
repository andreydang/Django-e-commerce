

from .views import (ProductListView,
                    ProductDetailSlugView, )

from django.urls import path, re_path
app_name = "products"
urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    re_path(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name='detail'),
]
