# Generated by Django 4.0.6 on 2023-02-21 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_friday_classend_alter_friday_classstart_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='disfriday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theclass', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='dismonday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theclass', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='disthursday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theclass', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='distuesday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theclass', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='diswednesday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theclass', models.CharField(max_length=32)),
            ],
        ),
    ]
