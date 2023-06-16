# Generated by Django 4.2.2 on 2023-06-08 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coursemodel',
            old_name='course',
            new_name='course_name',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='course',
            new_name='course_name',
        ),
        migrations.AlterField(
            model_name='teacher',
            name='photo',
            field=models.ImageField(upload_to='media/'),
        ),
    ]