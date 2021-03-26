from time import time

from django.db import models


def gen_slug():  # генерация слага
    return str(int(time()))


class Message(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    text = models.TextField('Текст', null=True, blank=True)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'


class Questions(models.Model):
    text = models.TextField(blank=True, max_length=1024)
    slug = models.SlugField(max_length=150, blank=True, default='', unique=True)
    date_pub = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug()
        super().save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.text)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ['-date_pub']
