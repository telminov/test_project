from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

import core.models
import core.forms
import core.filters


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

    def get_filters(self) -> core.filters.Book:
        return core.filters.Book(self.request.GET)

    def get_context_data(self, **kwargs):
        c = super().get_context_data()
        c['filters'] = self.get_filters()
        return c

    def get_queryset(self):
        return self.get_filters().qs


# class BookDetail(TitleMixin, DetailView):
#     queryset = core.models.Book.objects.all()
#
#     def get_title(self):
#         return str(self.get_object())


class BookCreate(TitleMixin, CreateView):
    title = 'Добавление книги'
    queryset = core.models.Book.objects.all()
    form_class = core.forms.BookEdit
    template_name = 'core/book_form.html'

    def get_success_url(self):
        return reverse('core:books')


class BookUpdate(TitleMixin, UpdateView):
    queryset = core.models.Book.objects.all()
    form_class = core.forms.BookEdit

    def get_title(self):
        return 'Обновление ' + str(self.get_object())

    def get_success_url(self):
        return reverse('core:books')


class BookDelete(TitleMixin, DeleteView):
    queryset = core.models.Book.objects.all()

    def get_title(self):
        return 'Удаление ' + str(self.get_object())

    def get_success_url(self):
        return reverse('core:books')
