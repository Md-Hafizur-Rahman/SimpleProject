# Generated by Django 4.0.1 on 2022-01-19 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuition', '0008_class_in_subject_post_class_in_post_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='details',
            field=models.TextField(max_length=30),
        ),
    ]
