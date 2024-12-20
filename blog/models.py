from django.db import models
from blog.utils import upload_to


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name="название")
    body = models.TextField(verbose_name="содержимое")
    image = models.ImageField(
        upload_to="blog_images/",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите изображение",
    )
    created_at = models.DateTimeField(
        auto_now_add=True, blank=True, null=True, verbose_name="Дата создания записи"
    )
    # updated_at = models.DateField(
    #     blank=True, null=True, verbose_name="Дата изменения записи"
    # )
    views_count = models.PositiveIntegerField(default=0, verbose_name="Просмотров")
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")
    slug = models.CharField(max_length=150, verbose_name="slug", null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "статья"
        verbose_name_plural = "статьи"
