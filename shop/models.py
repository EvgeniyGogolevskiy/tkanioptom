from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Gabardin(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    title = models.CharField(max_length=255, verbose_name='Название ткани', default='FUHUA')
    slug = models.SlugField(max_length=200, db_index=True, verbose_name='URL')
    color = models.CharField(max_length=255, verbose_name='Цвет')
    quantity = models.IntegerField(default=0, verbose_name='Количество')
    price = models.DecimalField(default=145, max_digits=10, decimal_places=2, verbose_name='Цена')
    available = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    def __str__(self):
        return self.color

    def get_absolute_url(self):
        return reverse('gabardin', kwargs={'g_slug': self.slug})

    class Meta:
        verbose_name = 'Габардин'
        verbose_name_plural = 'Габардин'
        index_together = (('id', 'slug'),)
        ordering = ['-quantity']
