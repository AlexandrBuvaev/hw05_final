# Generated by Django 2.2.16 on 2022-08-03 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_auto_20220803_0900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, help_text='Добавьте изображение к посту', null=True, upload_to='posts/', verbose_name='Картинка к посту'),
        ),
    ]
