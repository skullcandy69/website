# Generated by Django 3.0b1 on 2019-11-12 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Input',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(default='', max_length=100)),
                ('destination', models.CharField(default='', max_length=100)),
                ('date', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
