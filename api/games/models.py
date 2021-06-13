from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=40)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.name + ', ' + self.country


class Game(models.Model):
    title = models.CharField(max_length=30)
    pub_date = models.DateField()
    genre = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name='games')

    def __str__(self):
        return self.title
