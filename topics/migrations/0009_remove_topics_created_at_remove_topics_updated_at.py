# Generated by Django 5.0.7 on 2024-07-20 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0008_topics_created_at_topics_updated_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topics',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='topics',
            name='updated_at',
        ),
    ]