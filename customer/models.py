from uuid import uuid4
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
user = get_user_model()


class CustomerItem(models.Model):
    STATUS = (
        ('True', "فعال"),
        ("False", "غیرفعال")
    )
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name='عنوان')
    description = models.TextField(max_length=300, verbose_name='توضیحات')
    status = models.CharField(max_length=50, choices=STATUS, default=False, verbose_name='وضعیت')
    slug = models.SlugField(verbose_name='عبارت لینک', null=True,blank=True, unique=True, allow_unicode=True, max_length=200)
    update_at = models.DateTimeField(auto_now=True, verbose_name='آپدیت شده در تاریخ')

    def save(self):
        if self.slug == None:
            slug = self.title + '-' + uuid4().hex
            self.slug = slugify(slug)
        super(CustomerItem, self).save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ' مشکلات مشتری '
        verbose_name_plural = 'مشکلات مشتری ها'


class CustomerItemImage(models.Model):
    customer_item = models.ForeignKey(CustomerItem, on_delete=models.CASCADE)
    image_file = models.FileField(
        upload_to='images/product/',
        validators=[FileExtensionValidator(allowed_extensions=('jpg', 'png', 'jpeg'))],
        verbose_name="تصویر"
    )

    class Meta:
        verbose_name = 'تصویر محصول'
        verbose_name_plural = ' تصاویر محصول'
