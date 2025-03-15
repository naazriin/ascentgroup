from django.db import models

class DateMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Product(DateMixin):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='products')


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Products'
        verbose_name = 'Product'