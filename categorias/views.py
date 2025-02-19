from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms, serializers


class CategoriaListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Categoria
    template_name = 'categoria_list.html'
    context_object_name = 'categorias'
    paginate_by = 10
    permission_required = 'categorias.view_categoria'

    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.GET.get('nome')

        if nome:
            queryset = queryset.filter(name__icontains=nome)

        return queryset


class CategoriaCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Categoria
    template_name = 'categoria_create.html'
    form_class = forms.CategoriaForm
    success_url = reverse_lazy('categoria_list')
    permission_required = 'categorias.add_categoria'


class CategoriaDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Categoria
    template_name = 'categoria_detail.html'
    permission_required = 'categorias.view_category'


class CategoriaUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Categoria
    template_name = 'categoria_update.html'
    form_class = forms.CategoriaForm
    success_url = reverse_lazy('categoria_list')
    permission_required = 'categorias.change_category'


class CategoriaDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Categoria
    template_name = 'categoria_delete.html'
    success_url = reverse_lazy('categoria_list')
    permission_required = 'categorias.delete_category'


class CategoriaCreateListAPIView(generics.ListCreateAPIView):
    queryset = models.Categoria.objects.all()
    serializer_class = serializers.CategoriaSerializer


class CategoriaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Categoria.objects.all()
    serializer_class = serializers.CategoriaSerializer
