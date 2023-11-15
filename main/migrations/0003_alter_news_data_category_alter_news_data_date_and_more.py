# Generated by Django 4.2.2 on 2023-11-08 12:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0002_rename_news_news_data"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news_data",
            name="category",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="news_data",
            name="date",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="news_data",
            name="img",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="news_data",
            name="text",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="news_data",
            name="title",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="news_data",
            name="weather",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
