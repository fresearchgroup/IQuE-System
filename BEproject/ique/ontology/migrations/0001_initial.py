# Generated by Django 2.1rc1 on 2018-09-29 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=50)),
                ('owl', models.FileField(upload_to='files/owl')),
                ('los', models.FileField(upload_to='files/los')),
                ('ai', models.FileField(upload_to='files/ai')),

            ],
        ),
    ]
