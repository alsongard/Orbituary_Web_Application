# Generated by Django 5.1.3 on 2024-11-16 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=35)),
                ('middle_name', models.CharField(max_length=35)),
                ('last_name', models.CharField(max_length=35)),
                ('date_of_birth', models.DateField()),
                ('date_of_death', models.DateField()),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=35)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
