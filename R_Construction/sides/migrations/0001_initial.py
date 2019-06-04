# Generated by Django 2.2.1 on 2019-05-27 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SideIncharge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Side',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sideName', models.CharField(max_length=100)),
                ('sideAdd', models.TextField(blank=True, null=True)),
                ('vehicles', models.CharField(max_length=200)),
                ('activeVehicle', models.CharField(max_length=200)),
                ('employee', models.CharField(max_length=100)),
                ('sideIncharge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sides.SideIncharge')),
            ],
        ),
    ]
