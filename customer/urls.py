from django.urls import path
from . import views

urlpatterns = [
    path('', views.CustomerProfileView.as_view(), name='profile'),
    path('update/', views.update, name='update'),
    path('stuff/', views.CustomerStuffListView.as_view(), name='stuff'),
    path('request/', views.CustomerRequest.as_view(), name='request'),
    path('<slug:slug>', views.CustomerStuffDetail.as_view(), name='customer_stuff_detail')

]
