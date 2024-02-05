# Generated by Django 4.2.7 on 2024-02-04 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0005_alter_service_sid'),
    ]

    operations = [
        migrations.CreateModel(
            name='editprovider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('mailid', models.CharField(max_length=30)),
                ('service', models.CharField(max_length=20)),
                ('phone', models.IntegerField()),
                ('experience', models.CharField(max_length=50)),
                ('education', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('image', models.ImageField(upload_to='profileimages/')),
            ],
        ),
        migrations.RemoveField(
            model_name='appointments',
            name='appid',
        ),
        migrations.RemoveField(
            model_name='appointments',
            name='cid',
        ),
        migrations.RemoveField(
            model_name='appointments',
            name='cpayid',
        ),
        migrations.RemoveField(
            model_name='appointments',
            name='pid',
        ),
        migrations.RemoveField(
            model_name='appointments',
            name='sid',
        ),
        migrations.AddField(
            model_name='appointments',
            name='id',
            field=models.BigAutoField(auto_created=True, default=77, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
