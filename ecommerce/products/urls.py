

from .views import (ProductListView,
                    ProductDetailSlugView, )

from django.urls import path, re_path

urlpatterns = [
    path('', ProductListView.as_view()),
    re_path(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view()),
]
