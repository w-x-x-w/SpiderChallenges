# Generated by Django 5.0.7 on 2024-07-19 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0005_alter_topics_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topics',
            name='category',
            field=models.CharField(blank=True, default='成神之路', help_text='题目类别：成神之路，xpath特训', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='topics',
            name='difficulty',
            field=models.CharField(blank=True, choices=[('beginner', '初级'), ('intermediate', '中级'), ('advanced', '高级'), ('ultimate', '终极')], default='简单', help_text='难度', max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='topics',
            name='difficulty_score',
            field=models.BigIntegerField(blank=True, default=200, help_text='难度分数，后续根据此字段排序order_id', null=True),
        ),
        migrations.AlterField(
            model_name='topics',
            name='pass_status',
            field=models.BooleanField(blank=True, default=False, help_text='是否通过', null=True),
        ),
        migrations.AlterField(
            model_name='topics',
            name='points',
            field=models.TextField(blank=True, default='暂未更新考点', help_text='本题的考点', null=True),
        ),
        migrations.AlterField(
            model_name='topics',
            name='solution_txt',
            field=models.URLField(blank=True, default='暂无表述', help_text='图文讲解', null=True),
        ),
        migrations.AlterField(
            model_name='topics',
            name='solution_video',
            field=models.URLField(blank=True, default='暂无表述', help_text='视频讲解', null=True),
        ),
    ]
