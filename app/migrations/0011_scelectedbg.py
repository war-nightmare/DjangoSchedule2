# Generated by Django 4.2.1 on 2023-05-27 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0010_delete_pictest"),
    ]

    operations = [
        migrations.CreateModel(
            name="scelectedbg",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("bgname", models.CharField(max_length=64)),
            ],
        ),
    ]
