# Generated by Django 2.0 on 2017-12-10 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cases',
            name='vote_num',
            field=models.IntegerField(default=0, verbose_name='点赞数'),
        ),
    ]
