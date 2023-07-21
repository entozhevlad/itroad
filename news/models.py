from django.db import models

class Article(models.Model):
    title = models.CharField('Название', max_length=100, default = 50)
    anounce = models.CharField('Анонс', max_length= 300)
    full_text = models.TextField('Статья')
    date = models.DateField('Дата публикация')
    def __str__(self):
        return f'Новость: {self.title}'
    def get_absolute_url(self):
        return f'/news/{self.id}'
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
# Create your models here.
