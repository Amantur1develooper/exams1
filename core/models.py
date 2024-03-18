from django.db import models

# Create your models here.

class Tag(models.Model):

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'

    name = models.CharField(verbose_name='название', max_length=50, unique=True)

    def __str__(self):
        return f'{self.name}'


class Image(models.Model):
    
    class Meta:
        verbose_name = 'изображение'
        verbose_name_plural = 'изображении'
    product = models.ForeignKey('Product', on_delete=models.PROTECT, related_name='images', blank=True, null=True)
    name = models.CharField(max_length=70, verbose_name='название', unique=True, blank=True, null=True)
    image = models.ImageField(verbose_name='изображение', upload_to='images/', null=True)
    
    def __str__(self):
        return f'{self.name}'

        
class Category(models.Model):

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    name = models.CharField(verbose_name='название', max_length=50, unique=True)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

    title = models.CharField(max_length=100, verbose_name='имя')
    price = models.IntegerField(verbose_name='цена')
    content = models.TextField(verbose_name='контент')
    # images = models.ManyToManyField(Image, verbose_name='картинки')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='product', verbose_name='категория')
    tags = models.ManyToManyField('Tag', related_name='product', verbose_name='теги', blank=True)

    def __str__(self):
        return f'{self.title}'

class ProductAtribute(models.Model):

    class Meta:
        verbose_name = 'атрибут'
        verbose_name_plural = 'атрибуты'
    
    product = models.ForeignKey('Product', on_delete=models.PROTECT, related_name='atribute')
    name = models.CharField(max_length=50, verbose_name='ключ')
    value = models.CharField(max_length=150, verbose_name='значение')
    
    def __str__(self):
        return f'{self.name}-{self.value}'