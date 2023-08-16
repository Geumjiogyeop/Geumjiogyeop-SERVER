# Generated by Django 4.2.4 on 2023-08-15 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adoption', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='adoption',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='adoption',
            name='breed',
            field=models.BooleanField(default=False),
        ),
    ]
