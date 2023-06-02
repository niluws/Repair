# Generated by Django 4.2.1 on 2023-05-30 20:06

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
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
                ('en_title', models.CharField(max_length=50, verbose_name='عنوان انگلیسی')),
                ('slug', models.SlugField(allow_unicode=True, blank=True, max_length=200, unique=True, verbose_name='عبارت لینک')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='آپدیت شده در تاریخ')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='category.category', verbose_name='دسته\u200cمادر')),
            ],
            options={
                'verbose_name': 'دسته',
                'verbose_name_plural': 'دسته\u200cبندی\u200c',
            },
        ),
    ]