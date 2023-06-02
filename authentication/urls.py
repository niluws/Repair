from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('activation/<active_code>/', views.Activation.as_view(), name='activation'),
    path('logout/', views.Logout, name='logout'),

]
