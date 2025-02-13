# Generated by Django 3.2.24 on 2024-09-03 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_notification'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('FROMID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Fromid', to='myapp.login')),
                ('TOID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Toid', to='myapp.login')),
            ],
        ),
    ]
