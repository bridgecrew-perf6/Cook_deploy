# Generated by Django 4.0.4 on 2022-05-30 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cook', '0003_alter_recipe_directions_alter_recipe_ingredients_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=True, max_length=200, unique=True),
        ),
    ]