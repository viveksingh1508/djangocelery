# Generated by Django 5.2 on 2025-04-29 17:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asin', models.CharField(max_length=120, unique=True)),
                ('title', models.CharField(blank=True, max_length=220, null=True)),
                ('current_price', models.FloatField(blank=True, default=0.0, null=True)),
                ('metadata', models.JSONField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductScrapeEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True, max_length=500, null=True)),
                ('data', models.JSONField(blank=True, null=True)),
                ('asin', models.CharField(max_length=120, unique=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scrape_events', to='products.product')),
            ],
        ),
    ]
