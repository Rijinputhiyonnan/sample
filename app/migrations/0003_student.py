# Generated by Django 4.2.2 on 2023-06-09 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_course_coursemodel_course_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=255)),
                ('lname', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=10)),
                ('course_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.coursemodel')),
            ],
        ),
    ]
