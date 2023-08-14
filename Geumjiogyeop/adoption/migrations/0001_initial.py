# Generated by Django 4.2.4 on 2023-08-14 00:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adoption',
            fields=[
                ('adoption_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
                ('breed', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=1)),
                ('age', models.IntegerField(default=0)),
                ('weight', models.IntegerField(default=0)),
                ('is_neutralized', models.BooleanField(default=False)),
                ('center', models.CharField(max_length=50)),
                ('introduction', models.CharField(max_length=100)),
                ('letter', models.CharField(max_length=400)),
                ('photo', models.ImageField(blank=True, default='default_image.png', upload_to='')),
                ('likes', models.IntegerField(default=0)),
                ('contact_num', models.IntegerField(default=0)),
                ('adoption_availability', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserLikedAdoption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adoption', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adoption.adoption')),
            ],
        ),
    ]
