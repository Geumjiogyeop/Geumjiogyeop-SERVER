# Generated by Django 4.2.4 on 2023-08-14 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0004_alter_report_relation'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='etc',
            field=models.TextField(default='', verbose_name='기타이유'),
        ),
    ]