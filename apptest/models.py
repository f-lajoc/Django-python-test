from django.db import models

# Create your models here.
class ContactMessage(models.Model):
  fullname = models.CharField(max_length=250)
  email = models.EmailField()
  about = models.TextField()
  attended_to = models.BooleanField(default=False)
  def __str__(self):
    return f'Name: {self.fullname} || Email: {self.email}'