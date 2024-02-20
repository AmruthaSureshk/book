from django.forms import ModelForm
from . models import Author,Book,Review

class AuthorForm(ModelForm):
    class Meta:
        model=Author
        fields= '__all__'
        
class BookForm(ModelForm):
    class Meta:
        model=Book
        fields= '__all__'
    
class AuthorReviewForm(ModelForm):
    class Meta:
        model=Review
        fields= ['author','rating','comment']  
        
class BookReviewForm(ModelForm):
    class Meta:
        model=Review
        fields= ['book','rating','comment'] 