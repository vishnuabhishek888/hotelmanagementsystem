from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Room(models.Model):
    number = models.CharField(max_length=10)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.number

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    guest_name = models.CharField(max_length=100)

    def __str__(self):
        return self.guest_name
