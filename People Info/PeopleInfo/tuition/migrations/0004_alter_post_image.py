# Generated by Django 4.0.1 on 2022-01-18 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuition', '0003_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='tuition/images'),
        ),
    ]
