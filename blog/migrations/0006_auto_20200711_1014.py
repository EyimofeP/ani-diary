# Generated by Django 3.0.7 on 2020-07-11 09:14

from django.db import migrations, models
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200711_0727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='picture',
            field=models.ImageField(default='category/default.jpg', null=True, upload_to='category/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(blank=True, to='blog.Category', verbose_name='Category/Genre (Optional) e.g Love,Drama,HeartBreaking..'),
        ),
        migrations.AlterField(
            model_name='post',
            name='main_content',
            field=froala_editor.fields.FroalaField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, to='blog.Tag', verbose_name='Tags/Emotions (Optional)  e.g Sad,Happy, Funny'),
        ),
    ]
