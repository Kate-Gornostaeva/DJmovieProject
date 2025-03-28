from django.db import models


class Film(models.Model):
    name = models.CharField("Название фильма", max_length=150)
    description = models.TextField("Краткое содержание")
    review = models.TextField("Отзыв")

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"



# Create your models here.
