from django.urls import path
from . import views


urlpatterns = [
    path('categorias/listar/', views.CategoriaListView.as_view(), name='categoria_list'),
    path('categorias/cadastrar/', views.CategoriaCreateView.as_view(), name='categoria_create'),
    path('categorias/<int:pk>/detail/', views.CategoriaDetailView.as_view(), name='categoria_detail'),
    path('categorias/<int:pk>/update/', views.CategoriaUpdateView.as_view(), name='categoria_update'),
    path('categorias/<int:pk>/delete/', views.CategoriaDeleteView.as_view(), name='categoria_delete'),

    path('api/v1/categorias/', views.CategoriaCreateListAPIView.as_view(), name='categoria-create-list-api-view'),
    path('api/v1/categorias/<int:pk>/', views.CategoriaRetrieveUpdateDestroyAPIView.as_view(), name='categoria-detail-api-view'),
]
