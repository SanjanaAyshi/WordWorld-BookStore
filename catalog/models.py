from django.db import models

# Create your models here.
#table1:Category
class Category(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name
    
# Table 2: Publication (Publisher)
class Publication(models.Model):
    name=models.CharField(max_length=200)
    address=models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name
    
# Table 3: Author
class Author(models.Model):
    name=models.CharField(max_length=100)
    bio=models.TextField(blank=True,null=True)
    publication=models.ForeignKey(
        Publication,
        on_delete=models.SET_NULL,
        null=True,
        related_name='authors'
    )

    def __str__(self):
        return self.name
    
#Table 4: Book
class Book(models.Model):
    title=models.CharField(max_length=250)
    description=models.TextField(blank=True,null=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.IntegerField(default=0)
    isbn=models.CharField(max_length=20,unique=True)
    publicationDate=models.DateField(blank=True,null=True)
    category=models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='books'
    )
    author=models.ForeignKey(
        Author,
        on_delete=models.SET_NULL,
        null=True,
        related_name='books'
    )
    publication=models.ForeignKey(
        Publication,
        on_delete=models.SET_NULL,
        null=True,
        related_name='books'
    )

    def __str__(self):
        return self.title
    
