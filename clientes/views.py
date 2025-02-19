from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms, serializers
from rest_framework.permissions import IsAuthenticated


class ClienteListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Cliente
    template_name = 'cliente_list.html'
    context_object_name = 'clientes'
    paginate_by = 10
    permission_required = 'clientes.view_cliente'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('nome')  # Ordenando alfabeticamente por nome
        nome = self.request.GET.get('nome')

        if nome:
            queryset = queryset.filter(nome__icontains=nome)

        return queryset


class ClienteCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Cliente
    template_name = 'cliente_create.html'
    form_class = forms.ClienteForm
    success_url = reverse_lazy('cliente_list')
    permission_required = 'clientes.add_cliente'

    def form_valid(self, form):
        form.instance.operador_created = self.request.user
        return super().form_valid(form)


class ClienteDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Cliente
    template_name = 'cliente_detail.html'
    permission_required = 'clientes.view_cliente'


class ClienteUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Cliente
    template_name = 'cliente_update.html'
    form_class = forms.ClienteForm
    success_url = reverse_lazy('cliente_list')
    permission_required = 'clientes.change_cliente'

    def form_valid(self, form):
        form.instance.operador_updated = self.request.user  # Atualiza o operador apenas na edição
        return super().form_valid(form)


class ClienteDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Cliente
    template_name = 'cliente_delete.html'
    success_url = reverse_lazy('cliente_list')
    permission_required = 'clientes.delete_cliente'


class ClienteCreateListAPIView(generics.ListCreateAPIView):
    queryset = models.Cliente.objects.all()
    serializer_class = serializers.ClienteSerializer
    permission_classes = [IsAuthenticated]  # Garante que apenas usuários logados podem acessar

    def perform_create(self, serializer):
        serializer.save(
            operador_created=self.request.user,
            operador_updated=self.request.user
        )


class ClienteRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Cliente.objects.all()
    serializer_class = serializers.ClienteSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(operador_updated=self.request.user)
