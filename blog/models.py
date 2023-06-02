from uuid import uuid4
from django.db import models
from django.utils.text import slugify
from category.models import Category
from django.core.validators import FileExtensionValidator


class Item(models.Model):
    STATUS = (
        ('True', "فعال"),
        ("False", "غیرفعال")
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='دسته', null=True, blank=True)
    title = models.CharField(max_length=200, verbose_name='عنوان ')
    description = models.TextField(max_length=500, verbose_name='توضیحات')
    status = models.CharField(max_length=50, choices=STATUS, default=False, verbose_name='وضعیت')
    slug = models.SlugField(verbose_name='عبارت لینک', null=True,blank=True, unique=True, allow_unicode=True, max_length=200)
    update_at = models.DateTimeField(auto_now=True, verbose_name='آپدیت شده در تاریخ')

    def save(self):
        if self.slug == None:
            slug = self.title + '-' + uuid4().hex
            self.slug = slugify(slug)
        super(Item, self).save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'کار '
        verbose_name_plural = 'کار های من'




class ItemImage(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    image_file = models.FileField(
        upload_to='ItemImage',
        validators=[FileExtensionValidator(allowed_extensions=('jpg', 'png', 'jpeg'))],
        verbose_name="تصویر"
    )

    class Meta:
        verbose_name = 'تصویر محصول'
        verbose_name_plural = ' تصاویر محصول'


class Settings(models.Model):
    phone = models.CharField(max_length=256, unique=True, verbose_name='شماره تلفن')
    about = models.TextField(max_length=256, verbose_name='درباره ی من')

    class Meta:
        verbose_name = 'تنظیمات'
        verbose_name_plural = 'تنظیمات'
class Skill(models.Model):
    title = models.CharField(max_length=256, unique=True, verbose_name='مهارت')
    skills = models.ForeignKey(Settings, on_delete=models.CASCADE, verbose_name='مهارت های من')
