from rest_framework import serializers
from .models import Author, Book, Review

class AuthorSerializer(serializers.ModelSerializer):
    total_books = serializers.IntegerField(read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'total_rating', 'total_books']

class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.name', read_only=True)
    class Meta:
        model = Book
        fields = ['id', 'title', 'author_name', 'author', 'total_rating']

class ReviewSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.name', read_only=True)
    book_title= serializers.CharField(source='book.title', read_only=True)
    class Meta:
        model = Review
        fields = ['id',  'author_name', 'book_title','author', 'book', 'rating', 'comment']
