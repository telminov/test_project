from django.urls import path
import core.views

app_name = 'core'

urlpatterns = [
    path('', core.views.IndexView.as_view()),
    path('books/', core.views.BookList.as_view(), name='books'),
    path('books/<int:pk>/', core.views.BookDetail.as_view(), name='book_detail'),
]
