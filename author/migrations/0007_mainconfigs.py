# Generated by Django 3.0.7 on 2020-07-14 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0006_delete_mainconfig'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainConfigs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(null=True)),
                ('picture', models.ImageField(default='main/author.jpg', null=True, upload_to='main/photos')),
            ],
        ),
    ]
