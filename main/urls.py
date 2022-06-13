from django.urls import path
from main import views



urlpatterns = [
    path('', views.index, name="index" ),
    path('upload', views.upload, name="upload"),
    path('book/<int:id>', views.book_detail, name="book_detail"),
    path('books/ajax/get-departments', views.get_departments, name="get-departments")
]