# Generated by Django 3.2.12 on 2022-10-10 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YeySON', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('path', models.CharField(max_length=64)),
                ('content', models.TextField(max_length=4096)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('date', models.DateTimeField()),
                ('content', models.TextField(max_length=4096)),
            ],
        ),
    ]
