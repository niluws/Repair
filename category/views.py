from django.shortcuts import render
from django.views import View

from .models import Category


class CategoryView(View):
    def get(self, request):
        categories = Category.objects.filter(parent=None)

        return render(request, 'component/navbar.html', {
            'categories': categories,

        })
