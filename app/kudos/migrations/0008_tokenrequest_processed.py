# Generated by Django 2.2.3 on 2019-09-26 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kudos', '0007_tokenrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='tokenrequest',
            name='processed',
            field=models.BooleanField(default=False),
        ),
    ]