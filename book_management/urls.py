"""
URL configuration for book_management project.

"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from book_app.views import  BookViewSet, ReviewViewSet ,AuthorViewSet
from book_app import views

router = routers.DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.book,name='book'),
    path('authors/', views.author_list, name='author-list'),
    path('books/', views.book_list, name='book'),
    path('books/update<int:id>/', views.update, name="update"),
    path('books/delete<int:bookid>/', views.delete, name="delete"),
    path('reviews/', views.review_list, name='review-list'),
    path('author/<int:author_id>/reviews/', views.author_reviews, name='author_reviews'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

