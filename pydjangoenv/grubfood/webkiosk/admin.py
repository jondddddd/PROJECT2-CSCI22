from django.contrib import admin

# Register your models here.
from .models import Customer, Food, Orders

admin.site.register(Customer)
admin.site.register(Food)
admin.site.register(Orders)
