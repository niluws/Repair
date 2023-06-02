from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.SET_NULL,
                               verbose_name='دسته‌مادر')
    title = models.CharField(max_length=50, verbose_name='عنوان')
    en_title = models.CharField(max_length=50, verbose_name='عنوان انگلیسی')
    slug = models.SlugField(verbose_name='عبارت لینک', blank=True, null=False, unique=True, allow_unicode=True,
                            max_length=200)
    update_at = models.DateTimeField(auto_now=True, verbose_name='آپدیت شده در تاریخ')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته'
        verbose_name_plural = 'دسته‌بندی‌'


    def save(self, *args, **kwargs):
        is_slug = bool(Category.objects.filter(slug=self.en_title))
        if self.slug == '':
            if is_slug:
                self.slug = slugify(self.en_title + str(self.id))
            else:
                self.slug = slugify(self.en_title)
        super().save(*args, **kwargs)
