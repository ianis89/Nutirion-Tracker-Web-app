# Generated by Django 4.0.3 on 2022-03-29 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FreeCalorieCounter', '0009_remove_postfood_carbohydrate_remove_postfood_fats_and_more'),
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
