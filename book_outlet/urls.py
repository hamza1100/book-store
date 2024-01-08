from django.urls import path
from . import views

urlpatterns = [
        path("", views.index),
        # need to add slug property in db entries. therefore, app won't work now.
        path('<slug:slug>', views.book_detail, name='book-detail')
]