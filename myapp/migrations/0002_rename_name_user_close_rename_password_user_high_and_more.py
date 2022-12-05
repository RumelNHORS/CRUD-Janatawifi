# Generated by Django 4.1.3 on 2022-12-04 11:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='close',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='password',
            new_name='high',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='subject',
            new_name='low',
        ),
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.AddField(
            model_name='user',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='user',
            name='open',
            field=models.CharField(default=datetime.datetime(2022, 12, 4, 11, 3, 33, 771337, tzinfo=datetime.timezone.utc), max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='trade_code',
            field=models.CharField(default=datetime.datetime(2022, 12, 4, 11, 3, 54, 594531, tzinfo=datetime.timezone.utc), max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='volume',
            field=models.CharField(default=datetime.datetime(2022, 12, 4, 11, 4, 4, 929257, tzinfo=datetime.timezone.utc), max_length=50),
            preserve_default=False,
        ),
    ]
