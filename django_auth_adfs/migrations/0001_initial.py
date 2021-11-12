# Generated by Django 3.2.9 on 2021-11-12 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveDirectoryConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(default=False, verbose_name='Enable/Disable ActiveDirectory use')),
                ('client_id', models.CharField(blank=True, max_length=255, null=True)),
                ('client_secret', models.CharField(blank=True, max_length=255, null=True)),
                ('mirror_groups', models.BooleanField(default=True)),
                ('groups_claim', models.CharField(choices=[('roles', 'Directory Roles'), ('groups', 'Security Groups')], default='roles', max_length=255)),
                ('username_claim', models.CharField(choices=[('upn', 'UPN')], default='upn', max_length=255)),
                ('tenant_id', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
