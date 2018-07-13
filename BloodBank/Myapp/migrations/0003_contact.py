# Generated by Django 2.0.5 on 2018-07-01 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0002_auto_20180630_2128'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250)),
                ('Email', models.CharField(max_length=250)),
                ('Contact', models.CharField(max_length=250)),
                ('Message', models.CharField(max_length=250)),
                ('Date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Contact',
            },
        ),
    ]
