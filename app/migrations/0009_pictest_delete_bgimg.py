# Generated by Django 4.2.1 on 2023-05-27 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0008_bgimg"),
    ]

    operations = [
        migrations.CreateModel(
            name="PicTest",
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
                ("gpic", models.ImageField(upload_to="imgs")),
            ],
            options={
                "db_table": "pictest",
            },
        ),
        migrations.DeleteModel(
            name="bgimg",
        ),
    ]
