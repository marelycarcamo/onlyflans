# Generated by Django 5.0.6 on 2024-07-03 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_contactoempresa'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactoempresa',
            old_name='email',
            new_name='email_empresa',
        ),
        migrations.RenameField(
            model_name='contactoempresa',
            old_name='message',
            new_name='message_empresa',
        ),
        migrations.RenameField(
            model_name='contactoempresa',
            old_name='name',
            new_name='name_empresa',
        ),
        migrations.RenameField(
            model_name='contactoempresa',
            old_name='phone',
            new_name='phone_empresa',
        ),
        migrations.RemoveField(
            model_name='contactoempresa',
            name='created_at',
        ),
    ]
