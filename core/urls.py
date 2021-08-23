from django.urls import path
import core.views

app_name = 'core'

urlpatterns = [
    path('', core.views.IndexView.as_view()),
    path('books/', core.views.BookList.as_view(), name='books'),
    path('books/create/', core.views.BookCreate.as_view(), name='book_create'),
    # path('books/<int:pk>/', core.views.BookDetail.as_view(), name='book_detail'),
    path('books/<int:pk>/update/', core.views.BookUpdate.as_view(), name='book_update'),
    path('books/<int:pk>/delete/', core.views.BookDelete.as_view(), name='book_delete'),
]
