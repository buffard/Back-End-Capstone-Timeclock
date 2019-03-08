# Generated by Django 2.1.7 on 2019-03-08 18:07

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
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=12)),
                ('last_name', models.CharField(max_length=12)),
                ('pay_rate', models.IntegerField()),
                ('start_date', models.DateField(default=None, null=True)),
                ('end_date', models.DateField(default=None, null=True)),
                ('pin_code', models.IntegerField()),
                ('isActive', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=35)),
                ('address', models.CharField(max_length=75)),
                ('phone_number', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clock_in_time', models.TimeField(default=None, null=True)),
                ('clock_out_time', models.TimeField(default=None, null=True)),
                ('clock_in_date', models.DateField(default=None, null=True)),
                ('clock_out_date', models.DateField(default=None, null=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Employee')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Manager'),
        ),
    ]
