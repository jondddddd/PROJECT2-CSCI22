from django.db import models

# Create your models here.
class Customer(models.Model):
#this is the table
#primary key allows to call a specific field but in django would automatically makes one called id
    firstname = models.CharField(max_length = 20)
    lastname = models.CharField(max_length = 20)
    address = models.CharField(max_length = 100)
    city = models.CharField(max_length = 20)

    def __str__(self):
        return f'{self.id}:{self.firstname},{self.lastname},{self.address},{self.city}'
#we neeed to make a order model and a food model for the startproject
#when we call migrate, thats when the tables are created

class Food(models.Model):

    foodname = models.CharField(max_length = 100)
    fooddescription = models.CharField(max_length = 2000)
    foodprice = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f'{self.id}:{self.foodname},{self.fooddescription},{self.foodprice}'
#foreign keys


#on cascade means u also delete all the orders related to the thing deleted
class Orders(models.Model):
    PAYMENT_MODE_CHOICES = [
    ('CH','Cash'),
    ('CD','Card')
    ]
    orderdatetime = models.DateTimeField(auto_now_add=True)
    paymentmode = models.CharField(max_length = 2, choices=PAYMENT_MODE_CHOICES) #CH is cash and CD is card
    quantity = models.IntegerField()
    food= models.ForeignKey(Food, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}:{self.customer.firstname},{self.customer.lastname},{self.orderdatetime},{self.food.foodname},{self.paymentmode},{self.quantity}'
