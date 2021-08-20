from django.views.generic import TemplateView, ListView, DetailView

import core.models


class TitleMixin:
    title: str = None

    def get_title(self) -> str:
        return self.title

    def get_context_data(self, **kwargs):
        c = super().get_context_data()
        c['title'] = self.get_title()
        return c


class IndexView(TitleMixin, TemplateView):
    template_name = 'core/index.html'
    title = 'Главная'


class BookList(TitleMixin, ListView):
    title = 'Книги'

    def get_queryset(self):
        queryset = core.models.Book.objects.all()
        name = self.request.GET.get('name')
        if name:
            queryset = queryset.filter(name__istartswith=name)
        return queryset


class BookDetail(TitleMixin, DetailView):
    queryset = core.models.Book.objects.all()

    def get_title(self):
        return str(self.get_object())

