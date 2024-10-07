from django.db import models

# Create your models here.
class Login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    type=models.CharField(max_length=100)

class User(models.Model):
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    gender=models.CharField(max_length=20)
    idproof=models.CharField(max_length=300)
    post=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    image=models.CharField(max_length=400)


class Complaints(models.Model):
    USER=models.ForeignKey(User,on_delete=models.CASCADE,default='')
    complaints=models.CharField(max_length=400)
    date=models.DateField()
    reply=models.CharField(max_length=400)


class Owner(models.Model):
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    image = models.CharField(max_length=400)

class Property(models.Model):
    OWNER = models.ForeignKey(Owner, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    details = models.CharField(max_length=200)
    status = models.CharField(max_length=100)
    image = models.CharField(max_length=400)


class Booking(models.Model):
    PROPERTY = models.ForeignKey(Property, on_delete=models.CASCADE)
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

class Rating(models.Model):
    PROPERTY = models.ForeignKey(Property, on_delete=models.CASCADE)
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    rating = models.CharField(max_length=100)
    review = models.CharField(max_length=100)

class Notification(models.Model):
    date = models.CharField(max_length=100)
    notification = models.CharField(max_length=100)


class Chat(models.Model):
    FROMID= models.ForeignKey(Login,on_delete=models.CASCADE,related_name="Fromid")
    TOID= models.ForeignKey(Login,on_delete=models.CASCADE,related_name="Toid")
    message=models.CharField(max_length=100)
    date=models.DateField()