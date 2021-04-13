from django.db import models
from django.urls import reverse



# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=1000)
    summary = models.TextField(blank=False, null=False)
    featured = models.BooleanField(default=False)

    def get_absolute_url(self):
        # You can determine the path in at least two ways

        # the url/view of interest is:
        # path('product/<int:product_id>',
        #       dynamic_lookup_view,
        #       name='dynamic_lookup')

        # Method # 1 use hard coded path
        url1 = f'/product/{self.id}'

        # Method # 2 use reverse to get view name
        kwargs = {'product_id': self.id}
        url2 = reverse('products:dynamic_lookup', kwargs=kwargs)

        # print(f'{url1=}')
        # print(f'{url2=}')
        # print(f'{url1==url2=}')

        return url2
