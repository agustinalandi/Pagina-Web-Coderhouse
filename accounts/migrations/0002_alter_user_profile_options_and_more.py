# Generated by Django 4.0.4 on 2022-06-30 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user_profile',
            options={'verbose_name': 'perfil', 'verbose_name_plural': 'perfiles'},
        ),
        migrations.AddField(
            model_name='user_profile',
            name='profile_picture',
            field=models.ImageField(default=1, upload_to='profile_picture'),
            preserve_default=False,
        ),
    ]