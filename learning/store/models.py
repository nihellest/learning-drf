"""
Store App Models
"""

from django.db import models


class Commodity(models.Model):
    title = models.CharField(
        max_length=128,
        verbose_name="Заголовок"
    )
    body = models.TextField(
        max_length=512,
        verbose_name="Основная информация"
    )
    is_active = models.BooleanField(
        verbose_name="Опубликован",
        default=True
    )
    price = models.IntegerField(
        verbose_name="Цена"
    )
    
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ['title']
