from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=100)
    total_rating = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name

    def total_books(self):
        return self.book_set.count()

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    total_rating = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    def __str__(self):
        return self.title

class Review(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, blank=True, null=True)
    rating = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    comment = models.TextField()

    def save(self, *args, **kwargs):
        if self.author:
            author_reviews = Review.objects.filter(author=self.author)
            total_rating = sum(review.rating for review in author_reviews) / len(author_reviews) if author_reviews else 0.00
            self.author.total_rating = total_rating
            self.author.save()
        elif self.book:
            book_reviews = Review.objects.filter(book=self.book)
            total_rating = sum(review.rating for review in book_reviews) / len(book_reviews) if book_reviews else 0.00
            self.book.total_rating = total_rating
            self.book.save()
        super(Review, self).save(*args, **kwargs)

    def __str__(self):
        if self.author:
            return f"Review for Author: {self.author.name}"
        elif self.book:
            return f"Review for Book: {self.book.title}"

