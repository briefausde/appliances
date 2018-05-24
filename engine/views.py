from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.views import generic
from engine.models import Product


class MainPageView(generic.ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'engine/products.html'

    def get_queryset(self):
        return self.model.objects.all().order_by('-pk')


class ProductDetailView(generic.TemplateView):
    model = Product
    template_name = 'engine/product.html'

    def post(self, *args, **kwargs):
        product = self.get_object()
        product.update_clicks()
        return TemplateResponse(self.request, self.template_name, {'product': product})

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
        return context

    def get_queryset(self):
        order_by_clicks = self.request.GET.get('order_by_clicks')
        if order_by_clicks:
            return self.model.objects.filter(category__name=self.kwargs['category']).order_by(
                '-clicks' if order_by_clicks == "most" else 'clicks')
        return self.model.objects.filter(category__name=self.kwargs['category']).order_by('-pk')
