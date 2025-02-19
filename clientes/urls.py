from django.urls import path
from . import views

urlpatterns = [
    path('clientes/listar', views.ClienteListView.as_view(), name='cliente_list'),
    path('clientes/cadastrar/', views.ClienteCreateView.as_view(), name='cliente_create'),
    path('clientes/<int:pk>/detail/', views.ClienteDetailView.as_view(), name='cliente_detail'),
    path('clientes/<int:pk>/update/', views.ClienteUpdateView.as_view(), name='cliente_update'),
    path('clientes/<int:pk>/delete/', views.ClienteDeleteView.as_view(), name='cliente_delete'),

    path('api/v1/clientes/', views.ClienteCreateListAPIView.as_view(), name='cliente-create-list-api-view'),
    path('api/v1/clientes/<int:pk>/', views.ClienteRetrieveUpdateDestroyAPIView.as_view(), name='cliente-detail-api-view'),
]

