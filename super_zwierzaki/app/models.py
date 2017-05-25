from django.db import models


class User(models.Model):
    user_id  = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

class Category(models.Model):
    name = models.CharField(max_length=50, default="-")

class Card(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    card_type = models.ForeignKey(Category, on_delete=None)
    card_name = models.CharField(max_length=50, default="-")
    card_number = models.IntegerField()
    added_date = models.DateTimeField()
    



