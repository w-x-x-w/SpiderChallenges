# Generated by Django 5.0.7 on 2024-07-24 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0014_topics_created_at_topics_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='topics',
            name='api_type',
            field=models.CharField(blank=True, default='直接对应视图', help_text='此题目的接口类型：直接对应视图，访问一个接口判断后决定是否返回视图，返回一个视图+【多个】api', max_length=255, null=True),
        ),
    ]
