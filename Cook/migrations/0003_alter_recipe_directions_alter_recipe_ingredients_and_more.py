# Generated by Django 4.0.4 on 2022-05-30 08:04

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cook', '0002_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='directions',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='recipes', to='Cook.post'),
        ),
    ]