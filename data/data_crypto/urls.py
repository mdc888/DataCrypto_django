from django.urls import path
from . import views
app_name = 'data_crypto'
urlpatterns = [
    path('homepage/', views.data_list, name='list'),
    path('<slug:slug>/', views.data_detail, name='detail')
]