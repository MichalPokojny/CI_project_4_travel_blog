# Generated by Django 3.2.18 on 2023-03-16 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20230314_2114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comment_count',
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='Travel', max_length=255),
        ),
    ]
