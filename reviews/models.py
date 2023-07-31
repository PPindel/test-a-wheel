from django.db import models
from django.contrib.auth.models import User
from checkout.models import Order
from products.models import Product
from django.core.validators import MinValueValidator, MaxValueValidator

STATUS = ((0, "Draft"), (1, "Published"))


class Review(models.Model):
    title = models.CharField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now=True)
    review_text = models.TextField()
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='order', unique=True)  # noqa E501
    service = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='service')  # noqa E501
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=5)  # noqa E501
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="review", default=0)  # noqa E501
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
