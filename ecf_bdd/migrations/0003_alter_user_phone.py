# Generated by Django 3.2 on 2021-05-10 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecf_bdd', '0002_alter_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
