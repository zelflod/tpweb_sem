# Generated by Django 2.1.7 on 2019-04-02 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
