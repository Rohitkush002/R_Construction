from django.db import models

class SignUp(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    mobile = models.CharField(max_length=15)

    def __str__(self):
        return self.email
