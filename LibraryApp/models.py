from django.db import models
from faker import Faker


class Library(models.Model):
   id = models.AutoField(primary_key=True, verbose_name='ID')
   publisher = models.CharField(max_length = 50, verbose_name='Publisher')
   author = models.CharField(max_length = 50, verbose_name='Author')
   title = models.CharField(max_length = 100, verbose_name='Title')
   pageCount= models.IntegerField(default=10, verbose_name='Page Count')
   category = models.CharField(max_length = 50, verbose_name='Category')
   shelfLocation = models.CharField(max_length = 50, verbose_name='Shelf Location')
   publishedDate = models.DateField(verbose_name='Published Date')
   isInStock = models.BooleanField(default=True, verbose_name='is in stock')
   dateCheckedOut = models.DateField(verbose_name='Date Checked Out', auto_now=True)

   def __str__(self):
        return f"{self.title} {self.publishedDate}"
   
   class Meta:
      db_table = "library"
      verbose_name = 'Library'
      verbose_name_plural = 'Library'

   @staticmethod
   def faker_populate_library():
    '''
    Populate model with dummy values
    '''
    if Library.objects.all().count() >= 200:
       return
    
    fake = Faker()
    for _ in range(200):
        Library.objects.create(
        publisher=fake.name()[:50], 
        author=fake.name()[:50], 
        title=fake.text()[:100], 
        pageCount=fake.random_int(10, 1000),
        category=fake.word()[:50],
        shelfLocation=fake.word()[:50],
        publishedDate=fake.date_of_birth(),
        isInStock=fake.boolean(),
        dateCheckedOut=fake.date_of_birth())
    return
