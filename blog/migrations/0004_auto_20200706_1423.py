# Generated by Django 3.0.7 on 2020-07-06 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_main_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(blank=True, to='blog.Category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, to='blog.Tag'),
        ),
    ]
