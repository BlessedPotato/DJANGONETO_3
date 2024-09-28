from django.db import models
from django.utils.timezone import now


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.URLField()
    release_date = models.DateTimeField(max_length=50, default=now())
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=50, unique=True, blank=True)

