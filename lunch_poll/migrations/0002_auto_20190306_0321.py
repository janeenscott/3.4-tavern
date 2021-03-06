# Generated by Django 2.1.5 on 2019-03-06 03:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lunch_poll', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lunch',
            name='user',
        ),
        migrations.AddField(
            model_name='location',
            name='description',
            field=models.TextField(default=True),
        ),
        migrations.AddField(
            model_name='location',
            name='title',
            field=models.CharField(default='generic', max_length=100),
        ),
        migrations.AlterField(
            model_name='location',
            name='votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='lunch',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
