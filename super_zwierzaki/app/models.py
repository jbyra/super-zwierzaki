from django.db import models


class User(models.Model):
    user_id  = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

class Card(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    card_type = models.CharField(max_length=50)
    card_number = models.IntegerField()
    added_date = models.DateTimeField()
    



