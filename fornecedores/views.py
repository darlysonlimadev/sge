from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms, serializers


class FornecedorListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Fornecedor
    template_name = 'fornecedor_list.html'
    context_object_name = 'fornecedores'
    paginate_by = 10
    permission_required = 'fornecedores.view_supplier'

    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.GET.get('nome')

        if nome:
            queryset = queryset.filter(name__icontains=nome)

        return queryset


class FornecedorCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Fornecedor
    template_name = 'fornecedor_create.html'
    form_class = forms.FornecedorForm
    success_url = reverse_lazy('fornecedor_list')
    permission_required = 'fornecedores.add_fornecedor'


class FornecedorDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Fornecedor
    template_name = 'fornecedor_detail.html'
    permission_required = 'fornecedores.view_fornecedor'


class FornecedorUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Fornecedor
    template_name = 'fornecedor_update.html'
    form_class = forms.FornecedorForm
    success_url = reverse_lazy('fornecedor_list')
    permission_required = 'fornecedores.change_fornecedor'


class FornecedorDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Fornecedor
    template_name = 'fornecedor_delete.html'
    success_url = reverse_lazy('fornecedor_list')
    permission_required = 'fornecedores.delete_fornecedor'


class FornecedorCreateListAPIView(generics.ListCreateAPIView):
    queryset = models.Fornecedor.objects.all()
    serializer_class = serializers.FornecedorSerializer


class FornecedorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Fornecedor.objects.all()
    serializer_class = serializers.FornecedorSerializer
