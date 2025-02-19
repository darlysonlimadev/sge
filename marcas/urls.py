from django.urls import path
from . import views

urlpatterns = [
    path('marcas/listar', views.MarcaListView.as_view(), name='marca_list'),
    path('marcas/cadastrar/', views.MarcaCreateView.as_view(), name='marca_create'),
    path('marcas/<int:pk>/detail/', views.MarcaDetailView.as_view(), name='marca_detail'),
    path('marcas/<int:pk>/update/', views.MarcaUpdateView.as_view(), name='marca_update'),
    path('marcas/<int:pk>/delete/', views.MarcaDeleteView.as_view(), name='marca_delete'),

    path('api/v1/marcas/', views.MarcaCreateListAPIView.as_view(), name='marca-create-list-api-view'),
    path('api/v1/marcas/<int:pk>/', views.MarcaRetrieveUpdateDestroyAPIView.as_view(), name='marca-detail-api-view'),
]

