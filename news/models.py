from django.db import models
from django import forms
from django.core.validators import MinValueValidator

class Articles(models.Model):
    title = models.CharField('название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    text = models.TextField('Staty')
    date = models.DateTimeField('Data')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'


    class Meta:
        verbose_name='Новость'
        verbose_name_plural = 'Новости'



