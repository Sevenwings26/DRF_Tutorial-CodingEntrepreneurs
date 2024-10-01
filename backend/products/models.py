from django.db import models

# step 4
# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)

    # def __init__(self):
    #     self.title
    # serializers 
    @property
    def sale_price(self):
        return "%.2f" %(float(self.price) * 0.8)
        # this will be sent without serializing

    def get_discount(self):
        return "2000"

