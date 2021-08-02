#conatins the classes that would make the adding stuff
from django.forms import ModelForm
#helper clas that would help in creting forms
from .models import Customer, Food, Orders
class Foodform(ModelForm):
    class Meta:
        model = Food
        fields = ['foodname','fooddescription','foodprice']
class Ordersform(ModelForm):
    class Meta:
        model = Orders
        fields = ['paymentmode','quantity','food','customer']
class Customerform(ModelForm):
    class Meta:
        model = Customer
        fields = ['lastname','firstname','address','city']
