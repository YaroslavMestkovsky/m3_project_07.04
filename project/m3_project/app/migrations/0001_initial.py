# Generated by Django 2.2 on 2022-03-30 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Can change log entry', max_length=40)),
                ('content_type', models.CharField(default='log entry', max_length=40)),
                ('codename', models.CharField(default='change_logentry', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Can change log entry', max_length=40)),
                ('content_type', models.CharField(default='log entry', max_length=40)),
                ('codename', models.CharField(default='change_logentry', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Can change log entry', max_length=40)),
                ('content_type', models.CharField(default='log entry', max_length=40)),
                ('codename', models.CharField(default='change_logentry', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Can change log entry', max_length=40)),
                ('content_type', models.CharField(default='log entry', max_length=40)),
                ('codename', models.CharField(default='change_logentry', max_length=40)),
            ],
        ),
    ]
