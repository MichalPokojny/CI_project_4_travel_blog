# Generated by Django 3.2.18 on 2023-03-28 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.TextField(default='Travel'),
        ),
    ]
