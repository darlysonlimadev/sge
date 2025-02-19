from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from app import metrics
from marcas.models import Marca
from categorias.models import Categoria
from . import models, forms, serializers


class ProdutoListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Produto
    template_name = 'produto_list.html'
    context_object_name = 'produtos'
    paginate_by = 10
    permission_required = 'produtos.view_product'

    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.GET.get('nome')
        codigo = self.request.GET.get('codigo')
        categoria = self.request.GET.get('categoria')
        marca = self.request.GET.get('marca')

        if nome:
            queryset = queryset.filter(title__icontains=nome)
        if codigo:
            queryset = queryset.filter(serie_number__icontains=codigo)
        if categoria:
            queryset = queryset.filter(category_id=categoria)
        if marca:
            queryset = queryset.filter(brand__id=marca)

        return queryset

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['produtos_metrics'] = metrics.get_product_metrics()
    #     context['sales_metrics'] = metrics.get_sales_metrics()
    #     context['categorias'] = Categoria.objects.all()
    #     context['marcas'] = Marca.objects.all()
    #     return context


class ProdutoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Produto
    template_name = 'produto_create.html'
    form_class = forms.ProdutoForm
    success_url = reverse_lazy('produto_list')
    permission_required = 'produtos.add_product'


class ProdutoDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Produto
    template_name = 'produto_detail.html'
    permission_required = 'produtos.view_product'


class ProdutoUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Produto
    template_name = 'produto_update.html'
    form_class = forms.ProdutoForm
    success_url = reverse_lazy('produto_list')
    permission_required = 'produtos.change_product'


class ProdutoDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Produto
    template_name = 'produto_delete.html'
    success_url = reverse_lazy('produto_list')
    permission_required = 'produtos.delete_product'


class ProdutoCreateListAPIView(generics.ListCreateAPIView):
    queryset = models.Produto.objects.all()
    serializer_class = serializers.ProdutoSerializer


class ProdutoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Produto.objects.all()
    serializer_class = serializers.ProdutoSerializer
