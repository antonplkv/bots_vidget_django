# Generated by Django 2.1.7 on 2019-02-26 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vidget', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='img',
            new_name='img_url',
        ),
        migrations.AddField(
            model_name='user',
            name='user_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]