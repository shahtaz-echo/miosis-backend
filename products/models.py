from django.db import models
from base.models import BaseModel

# Product model
class Product(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.title
    
    @property
    def is_in_stock(self) -> bool:
        return self.stock>0
    
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Products'
