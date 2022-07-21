# Generated by Django 4.0.4 on 2022-04-30 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('desc', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='contact',
        ),
    ]
