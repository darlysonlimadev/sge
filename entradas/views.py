from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from . import models, forms, serializers


class EntradaListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Entrada
    template_name = 'entrada_list.html'
    context_object_name = 'entradas'
    paginate_by = 10
    permission_required = 'entradas.view_entrada'

    def get_queryset(self):
        queryset = super().get_queryset()
        produto = self.request.GET.get('produto')

        if produto:
            queryset = queryset.filter(produto__nome__icontains=produto)

        return queryset


class EntradaCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Entrada
    template_name = 'entrada_create.html'
    form_class = forms.EntradaForm
    success_url = reverse_lazy('entrada_list')
    permission_required = 'entradas.add_entrada'


class EntradaDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Entrada
    template_name = 'entrada_detail.html'
    permission_required = 'entradas.view_entrada'


class EntradaCreateListAPIView(generics.ListCreateAPIView):
    queryset = models.Entrada.objects.all()
    serializer_class = serializers.EntradaSerializer


class EntradaRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.Entrada.objects.all()
    serializer_class = serializers.EntradaSerializer
