from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.MainPageView.as_view(), name='main_page'),
    url(r'^product/(?P<pk>[0-9]+)/$', views.ProductDetailView.as_view(), name='product_detail'),
    url(r'^category/(?P<category>[-\w]+)$', views.ProductsListView.as_view(), name='products_list')
]
