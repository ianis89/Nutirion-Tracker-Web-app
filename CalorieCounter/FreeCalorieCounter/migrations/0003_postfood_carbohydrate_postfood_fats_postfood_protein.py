# Generated by Django 4.0.3 on 2022-03-28 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FreeCalorieCounter', '0002_food_carbohydrate_food_fats_food_protein'),
    ]

    operations = [
        migrations.AddField(
            model_name='postfood',
            name='carbohydrate',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AddField(
            model_name='postfood',
            name='fats',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AddField(
            model_name='postfood',
            name='protein',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
