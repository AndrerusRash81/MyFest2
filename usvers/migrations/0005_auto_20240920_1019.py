# Generated by Django 3.1.8 on 2024-09-20 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usvers', '0004_bdusvers_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bdrol',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='bdusvers',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='bdusvers',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='bdusvers',
            name='infa',
            field=models.FileField(blank=True, null=True, upload_to='doc/'),
        ),
    ]
