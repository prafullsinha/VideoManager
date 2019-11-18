# Generated by Django 2.2.7 on 2019-11-15 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VideoModel',
            fields=[
                ('title', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('categories', models.CharField(blank=True, max_length=15)),
                ('tags', models.CharField(blank=True, max_length=20)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('duration', models.TimeField(blank=True)),
                ('description', models.CharField(blank=True, max_length=30)),
                ('thumbnail', models.FileField(blank=True, upload_to='images/', verbose_name='')),
                ('videofile', models.FileField(null=True, upload_to='videos/', verbose_name='')),
            ],
        ),
    ]
