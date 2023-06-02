from django.urls import path

from blog import views

urlpatterns = [
    path('<category>', views.Blog.as_view(), name='category'),
]
