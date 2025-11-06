from django.db import models
from django.contrib.auth.models import User
from auth_system.models import User

# Create your models here.
class Room(models.Model):
    type_choise = [
        ('standart', 'Standart'),
        ('lux', 'Lux'),
        ('suite', 'Suite'),
        ('family', 'Family'),
        ('single', 'Single'),
        ('double', 'Double'),
        ('twin', 'Twin'),
        ('deluxe', 'Deluxe'),
        ('presidential', 'Presidential'),
        ('penthouse', 'Penthouse'),
        ('cottage', 'Cottage'),
        ('villa', 'Villa'),
        ('bungalow', 'Bungalow'),
        ('hostel', 'Hostel'),
        ('dormitory', 'Dormitory'),
        ('capsule', 'Capsule'),
        ('igloo', 'Igloo'),
        ('treehouse', 'Treehouse'),
        ('yurt', 'Yurt'),
        ('cabin', 'Cabin'),
        ('chalet', 'Chalet'),
        ('farmstay', 'Farmstay'),
        ('glamping', 'Glamping'),
        ('ryokan', 'Ryokan'),
        ('pousada', 'Pousada'),
        ('parador', 'Parador'),
        ('auberge', 'Auberge'),
        ('hostal', 'Hostal'),
        ('motel', 'Motel'),
        ('inn', 'Inn'),
        ('guesthouse', 'Guesthouse'),
    ]
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    capacity = models.IntegerField(default=1)
    image = models.ImageField(upload_to='room_images/', null=True, blank=True)
    type_room = models.CharField(choices=type_choise, max_length=100, default='standart')

    def __str__(self):
        return self.title

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    persons = models.IntegerField(default=1)
    phone_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Кімната: {self.room} - Дата заїзду: {self.check_in} - Дата виїзду: {self.check_out} - Кількість осіб: {self.persons}'