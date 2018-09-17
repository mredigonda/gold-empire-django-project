# Generated by Django 2.1.1 on 2018-09-17 03:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('game', '0002_auto_20180916_0156'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('explorer', models.PositiveIntegerField(default=0)),
                ('footman', models.PositiveIntegerField(default=0)),
                ('rifleman', models.PositiveIntegerField(default=0)),
                ('almirant', models.PositiveIntegerField(default=0)),
                ('assassin', models.PositiveIntegerField(default=0)),
                ('samurai', models.PositiveIntegerField(default=0)),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
