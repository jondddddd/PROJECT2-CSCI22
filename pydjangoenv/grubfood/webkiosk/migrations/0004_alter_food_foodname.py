# Generated by Django 3.2.5 on 2021-08-02 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webkiosk', '0003_alter_food_fooddescription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='foodname',
            field=models.CharField(max_length=100),
        ),
    ]
