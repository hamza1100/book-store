from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default='', null=False, db_index=True)

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

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
    # Book.objects.get() => gets only 1 value, if there are 2 that matches criteria => throws error
    # To get multiple entries based on the searched criteria
        # Book.objects.filter(criteria)
    # less than|less than equal => filter(criteria__lt|lte=3)

    # from django.db.models import Q (or operator)
        # Book.objects.filter(Q(rating__lt=3) | Q(is_bestselling=True))
