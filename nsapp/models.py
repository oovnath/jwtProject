from django.db import models

# Create your models here.
class Instructor(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.email
    

class Course(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField()
    instructor = models.ForeignKey(Instructor,  on_delete=models.CASCADE, related_name = 'courses')
