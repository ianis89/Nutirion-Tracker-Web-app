# Generated by Django 4.0.3 on 2022-03-29 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FreeCalorieCounter', '0008_profile_carbohydrate_profile_fats_profile_protein'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postfood',
            name='carbohydrate',
        ),
        migrations.RemoveField(
            model_name='postfood',
            name='fats',
        ),
        migrations.RemoveField(
            model_name='postfood',
            name='protein',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='carbohydrate',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='fats',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='protein',
        ),
    ]
