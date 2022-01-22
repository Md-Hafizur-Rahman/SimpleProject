# Generated by Django 4.0.1 on 2022-01-18 17:32

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tuition', '0004_alter_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='MEDIUM',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('bangla', 'bangla'), ('english', 'english'), ('urdu', 'urdu'), ('hindi', 'hindi')], default='bangla', max_length=100),
        ),
    ]
