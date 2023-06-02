from django.views.generic import DetailView

from blog.models import Item
from category.models import Category

class Detail(DetailView):
    template_name = 'detail/detail.html'
    model = Item
    context_object_name = 'detailItems'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['categories'] = Category.objects.filter(parent=None)
        context['recent_items'] = Item.objects.order_by('-id')[:4]
        return context

