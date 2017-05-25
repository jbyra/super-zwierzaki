from django.db import models


class User(models.Model):
    user_id  = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

class Category(models.Model):
    name = models.CharField(max_length=50, default="-")

    def __str__(self):
        return self.name

class Card(models.Model):
    owner = models.ForeignKey('auth.User')
    card_type = models.ForeignKey(Category, on_delete=None)
    card_name = models.CharField(max_length=50, default="-")
    card_number = models.IntegerField()
    added_date = models.DateTimeField()

    def __str__(self):
        return self.card_name
    



