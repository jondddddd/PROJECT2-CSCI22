#conatins the classes that would make the adding stuff
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
#helper clas that would help in creting forms
from .models import Customer, Food, Orders
from django.contrib.auth.models import User
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
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
