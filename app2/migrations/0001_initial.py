# Generated by Django 3.2.8 on 2022-01-31 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='loginSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('passowrd', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=255)),
            ],
        ),
    ]
