from django.views.generic import TemplateView, ListView, DetailView

import core.models


class IndexView(TemplateView):
    template_name = 'core/index.html'


class BookList(ListView):
    def get_queryset(self):
        queryset = core.models.Book.objects.all()
        name = self.request.GET.get('name')
        if name:
            queryset = queryset.filter(name__istartswith=name)
        return queryset


class BookDetail(DetailView):
    queryset = core.models.Book.objects.all()

