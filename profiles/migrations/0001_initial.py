# Generated by Django 4.0.4 on 2022-08-02 12:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(blank=True, max_length=100)),
                ('bio', models.TextField(blank=True, max_length=300)),
                ('current_city', models.TextField(blank=True, max_length=256)),
                ('home_town', models.TextField(blank=True, max_length=256)),
                ('workplace', models.CharField(blank=True, max_length=100)),
                ('school', models.CharField(blank=True, max_length=100)),
                ('contact_info', models.CharField(blank=True, max_length=20)),
                ('realtionship_status', models.CharField(blank=True, max_length=20)),
                ('dob', models.DateField(blank=True)),
                ('profile_pic', models.ImageField(default='Blank_Profile_Pic.png', upload_to='profile_images')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
