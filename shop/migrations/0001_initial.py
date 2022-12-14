# Generated by Django 4.1.1 on 2022-09-17 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Gabardin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='FUHUA', max_length=255, verbose_name='Название ткани')),
                ('slug', models.SlugField(max_length=200)),
                ('color', models.CharField(max_length=255, verbose_name='Цвет')),
                ('quantity', models.IntegerField(default=0, verbose_name='Количество')),
                ('price', models.DecimalField(decimal_places=2, default=145, max_digits=10, verbose_name='Цена')),
                ('available', models.BooleanField(default=True)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Габардин',
                'verbose_name_plural': 'Габардин',
                'ordering': ['-quantity'],
                'index_together': {('id', 'slug')},
            },
        ),
    ]
