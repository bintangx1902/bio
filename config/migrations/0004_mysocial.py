# Generated by Django 3.1.7 on 2021-04-02 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0003_auto_20210402_1516'),
    ]

    operations = [
        migrations.CreateModel(
            name='MySocial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
            ],
        ),
    ]
