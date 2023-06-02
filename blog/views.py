from django.shortcuts import render, redirect, reverse
from django.views.generic.list import ListView
from category.models import Category
from .models import Item,Settings


class Blog(ListView):
    template_name = 'blog/blog.html'
    model = Item
    context_object_name = 'Items'

    paginate_by = 10
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['categories'] = Category.objects.filter(parent=None)
        return context
    def get_queryset(self):
        query = super(Blog, self).get_queryset()
        category_name = self.kwargs.get('category')
        if category_name is not None:
            query = query.filter(category__slug__iexact=category_name)
        return query
def about(request):
    settings=Settings.objects.all()
    return render(request,'blog/about.html',{'settings':settings})