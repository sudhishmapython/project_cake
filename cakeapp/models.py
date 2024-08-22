from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_owner=models.BooleanField(default=False)
    is_user=models.BooleanField(default=False)


class Owner(models.Model):
    user=models.ForeignKey(Login,on_delete=models.CASCADE,related_name='owners')
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    address=models.CharField(max_length=100)
    phone_no=models.CharField(max_length=100)

class Client(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE,related_name='users')
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=100)

class Category(models.Model):
    name=models.CharField(max_length=250)
    discription=models.TextField()

    def __str__(self):
        return self.name

class Cake(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="cakes")
    name=models.CharField(max_length=250)
    discription=models.CharField(max_length=250)
    price=models.IntegerField()
    stock=models.IntegerField(default=0)
    image=models.FileField(upload_to='uploads/')


class CartItem(models.Model):
    cake = models.ForeignKey(Cake, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} x {self.cake.name}'