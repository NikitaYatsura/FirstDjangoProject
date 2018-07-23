from django.db import models

# Create your models here.

class Lot(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    date_open = models.DateTimeField()
    date_close = models.DateTimeField()
    department = models.ForeignKey(
        'Section',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

class Section(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.name