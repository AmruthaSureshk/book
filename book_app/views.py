from rest_framework import viewsets, permissions
from .models import Author, Book, Review
from .serializers import AuthorSerializer, BookSerializer, ReviewSerializer
from django.shortcuts import redirect, render
from . forms import AuthorForm,BookForm,AuthorReviewForm,BookReviewForm

def book(request):
    
    return render(request,'api.html')

def author_list(request):
    authors = Author.objects.all()
    serializer = AuthorSerializer(authors, many=True)
    
    frm=AuthorForm()
    if request.POST:
        frm=AuthorForm(request.POST,request.FILES)
        if frm.is_valid():
            frm.save()
        else:
            frm=AuthorForm()
        return redirect('/authors')    
    return render(request, 'authors.html', {'authors': serializer.data,'frm': frm})


def book_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    
    bukfrm=BookForm()
    if request.POST:
        bukfrm=BookForm(request.POST,request.FILES)
        if bukfrm.is_valid():
            bukfrm.save()
        else:
            bukfrm=BookForm()
            
        return redirect('/books')
    
    return render(request, 'books.html', {'books': serializer.data , 'bukfrm': bukfrm})

def update(request, id):
    task=Book.objects.get(id=id)
    f=BookForm(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/books')
    return render(request,'edit.html',{'f':f,'task':task})

def delete(request,bookid):
    task=Book.objects.get(id=bookid)
    if request.method=='POST':
        task.delete()
        return redirect('/books')
    return render(request,'delete.html')


def review_list(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    
    authors = Author.objects.all()
    authorreviewfrm=AuthorReviewForm()
    if request.POST:
        authorreviewfrm=AuthorReviewForm(request.POST,request.FILES)
        if authorreviewfrm.is_valid():
            authorreviewfrm.save()
        else:
            authorreviewfrm=AuthorReviewForm()
            
        return redirect('/reviews')
    
    bookreviewfrm=BookReviewForm()
    if request.POST:
        bookreviewfrm=BookReviewForm(request.POST,request.FILES)
        if bookreviewfrm.is_valid():
            bookreviewfrm.save()
        else:
            bookreviewfrm=BookReviewForm()
            
        return redirect('/reviews')
    return render(request, 'reviews.html', {'reviews': serializer.data,'authorreviewfrm':authorreviewfrm,'bookreviewfrm':bookreviewfrm,'authors': authors})

def author_reviews(request, author_id):
    author_reviews = Review.objects.filter(author_id=author_id)
    return render(request, 'author_reviews.html', {'author_reviews': author_reviews})


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]
