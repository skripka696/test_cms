from django.db import models
from django.conf import settings


class Style(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class StyleValue(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    style = models.ForeignKey(Style)
    value = models.CharField(max_length=255)

    def __str__(self):
        return '{} - {}'.format(self.style.name, self.name if self.name else self.value)


class Field(models.Model):
    description = models.CharField(max_length=255)
    tag = models.CharField(max_length=255)
    style = models.ManyToManyField(StyleValue, blank=True, null=True)

    def __str__(self):
        return self.description


class Article(models.Model):
    ACCESS_CHOICES = (
        ('public', 'public'),
        ('official', 'official')
    )
    STATUS_CHOICES = (
        ('in_progress', 'in_progress'),
        ('published', 'published')
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='in_progress')
    access = models.CharField(max_length=50, choices=ACCESS_CHOICES, default='public')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user


class ArticleContent(models.Model):
    LANGUAGE_CHOICES = (
        ('ru', 'russian'),
        ('uk', 'ukrainian')
    )
    field = models.ManyToManyField(Field)
    article = models.ForeignKey(Article)
    text_value = models.TextField(blank=True, null=True)
    language = models.CharField(max_length=50, choices=LANGUAGE_CHOICES, default='ru')


class Revision(models.Model):
    article = models.ForeignKey(Article)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return self.user