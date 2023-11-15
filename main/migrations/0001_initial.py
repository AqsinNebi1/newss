# Generated by Django 4.2.2 on 2023-11-08 12:31

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="News",
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
                ("title", models.CharField(max_length=200)),
                ("text", models.TextField()),
                ("category", models.CharField(max_length=100)),
                ("img", models.CharField(max_length=100)),
                ("date", models.CharField(max_length=50)),
                ("weather", models.CharField(max_length=50)),
            ],
        ),
    ]