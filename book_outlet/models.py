from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)

    # when print with Book.objects.all()
    # it was displaying cryptic output
    # override this class function to display
    # in a human readable format
    def __str__(self):
        return f"{self.title} ({self.rating})"
    

# to enter in shell
    # python3 manage.py shell
    # from book_outlet.models import Book
    # Book.objects.all()/first()/last()