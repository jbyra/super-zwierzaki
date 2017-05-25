from django.db import models


class User(models.Model):
    user_id  = models.CharField(max_length=50)
    location = models.CharField(max_length=50)


class Card(models.Model):
    CARD_TYPE_CHOICES = {
        ('0', 'Najinteligentniejsze'),
        ('1', 'Najgłośniejsze'),
        ('2', 'Najbardziej efektowne'),
        ('3', 'Najszybsze'),
        ('4', 'Najdziwniejsze'),
        ('5', 'Najgroźniejsze')
    }

    owner = models.ForeignKey('auth.User')
    card_type = models.CharField(max_length=50, choices=CARD_TYPE_CHOICES)
    card_name = models.CharField(max_length=50, default="-")
    card_number = models.IntegerField()
    added_date = models.DateTimeField()

    def __str__(self):
        return self.card_name
    



