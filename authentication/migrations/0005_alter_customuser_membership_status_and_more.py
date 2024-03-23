# Generated by Django 5.0.2 on 2024-03-22 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_alter_customuser_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='membership_status',
            field=models.CharField(choices=[('free', 'Free'), ('plus', 'Plus'), ('premium', 'Premium')], default='free', max_length=10),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('client', 'Client'), ('worker', 'Worker')], default='client', max_length=10),
        ),
    ]
