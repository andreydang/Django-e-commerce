from .views import SearchProductView

from django.urls import path, re_path
app_name = "products"
urlpatterns = [
    path('', SearchProductView.as_view(), name='query'),

]
