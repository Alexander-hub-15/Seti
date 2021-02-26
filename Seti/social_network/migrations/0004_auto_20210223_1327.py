# Generated by Django 3.1.7 on 2021-02-23 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_network', '0003_auto_20210217_1615'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilesAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adminupload', models.FileField(upload_to='media')),
                ('title', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Документ',
                'verbose_name_plural': 'Документы',
            },
        ),
        migrations.DeleteModel(
            name='Document',
        ),
    ]
