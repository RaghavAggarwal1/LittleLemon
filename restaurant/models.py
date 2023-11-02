from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.PositiveIntegerField()
    booking_date = models.DateTimeField(auto_now_add=True)
    # reservation_slot = models.SmallIntegerField(default=10)

    def __str__(self): 
        return self.name

# Add code to create Menu model
class Menu(models.Model):
   title = models.CharField(max_length=255) 
   price = models.DecimalField(max_digits=10, decimal_places=2) 
   inventory = models.PositiveIntegerField() 
   
   def __str__(self):
       return self.title
   
   def get_item(self):
       return f'{self.title} : {str(self.price)}'