from django.http import JsonResponse
from django.shortcuts import redirect
from django.views import generic
from .models import Product


class MainPageView(generic.ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'engine/products.html'

    def get_queryset(self):
        return self.model.objects.all().order_by('-pk')


class ProductDetailView(generic.View):
    model = Product

    def post(self, *args, **kwargs):
        product = self.get_object()
        clicks = product.clicks + 1
        product.update_clicks()

        data = {
            'product_img': product.img,
            'product_category': product.category.name.upper(),
            'product_name': product.name.title(),
            'product_description': product.description,
            'product_price': product.price,
            'product_clicks': clicks,
            'product_created_date': "{}-{}-{}".format(
                product.created_date.year, product.created_date.month, product.created_date.day)
        }

        return JsonResponse(data)

    def get(self, *args, **kwargs):
        return redirect('/')

    def get_object(self):
        return self.model.objects.get(pk=self.kwargs['pk'])


class ProductsListView(generic.ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'engine/products.html'

    def get_context_data(self, **kwargs):
        context = super(ProductsListView, self).get_context_data(**kwargs)
        context['category'] = self.kwargs['category']

        if self.request.GET.get('order_by_clicks'):
            context['sorted'] = self.request.GET.get('order_by_clicks')

        return context

    def get_queryset(self):
        if self.request.GET.get('order_by_clicks'):
            return self.model.objects.filter(category__name=self.kwargs['category']).order_by(
                '-clicks' if self.request.GET.get('order_by_clicks') == "most" else 'clicks')
        return self.model.objects.filter(category__name=self.kwargs['category']).order_by('-pk')
