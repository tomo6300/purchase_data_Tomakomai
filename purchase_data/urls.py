from django.urls import path
from . import views
 
app_name = 'purchase_data'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    #path('index/', views.IndexView.as_view(), name='index'),
    path('item/create/', views.ItemCreateView.as_view(), name='item_create'),
    path('item/create/complete', views.ItemCreateCompleteView.as_view(), name='item_create_complete'),
    path('item/list/', views.ItemListView.as_view(),name='item_list'),
    path('item/detail/<uuid:pk>/', views.ItemDetailView.as_view(), name='item_detail'), 
    path('item/update/<uuid:pk>/', views.ItemUpdateView.as_view(), name='item_update'),
    path('item/delete/<uuid:pk>/', views.ItemDeleteView.as_view(), name='item_delete'),
    path('purchase_data/create/', views.PurchaseDataCreateView.as_view(), name='purchase_data_create'),
    path('purchase_data/create/complete', views.PurchaseDataCreateCompleteView.as_view(), name='purchase_data_create_complete'),
    path('purchase_data/list/', views.PurchaseDataListView.as_view(),name='purchase_data_list'),
    path('purchase_data/detail/<uuid:pk>/', views.PurchaseDataDetailView.as_view(), name='purchase_data_detail'), 
    path('purchase_data/update/<uuid:pk>/', views.PurchaseDataUpdateView.as_view(), name='purchase_data_update'),
    path('purchase_data/delete/<uuid:pk>/', views.PurchaseDataDeleteView.as_view(), name='purchase_data_delete'),
]