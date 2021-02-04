# Generated by Django 3.1.6 on 2021-02-04 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('subject', models.CharField(max_length=50)),
                ('visible', models.BooleanField(default=False)),
            ],
        ),
    ]
