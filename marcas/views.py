from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms, serializers


class MarcaListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Marca
    template_name = 'marca_list.html'
    context_object_name = 'marcas'
    paginate_by = 10
    permission_required = 'marcas.view_marca'

    def get_queryset(self):
        queryset = super().get_queryset()
        nome = self.request.GET.get('nome')

        if nome:
            queryset = queryset.filter(nome__icontains=nome)

        return queryset


class MarcaCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Marca
    template_name = 'marca_create.html'
    form_class = forms.MarcaForm
    success_url = reverse_lazy('marca_list')
    permission_required = 'marcas.add_marca'


class MarcaDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Marca
    template_name = 'marca_detail.html'
    permission_required = 'marcas.view_marca'


class MarcaUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Marca
    template_name = 'marca_update.html'
    form_class = forms.MarcaForm
    success_url = reverse_lazy('marca_list')
    permission_required = 'marcas.change_marca'


class MarcaDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Marca
    template_name = 'marca_delete.html'
    success_url = reverse_lazy('marca_list')
    permission_required = 'marcas.delete_marca'


class MarcaCreateListAPIView(generics.ListCreateAPIView):
    queryset = models.Marca.objects.all()
    serializer_class = serializers.MarcaSerializer


class MarcaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Marca.objects.all()
    serializer_class = serializers.MarcaSerializer
