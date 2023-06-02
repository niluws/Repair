from django.urls import path

from . import views

urlpatterns = [
    path('<slug:slug>', views.Detail.as_view(), name='detail')
]
