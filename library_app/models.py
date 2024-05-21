from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    author = models.ForeignKey('Author',on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name