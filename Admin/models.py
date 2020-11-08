from django.db import models
import qrcode
from random import randint
from django.template.defaultfilters import slugify

qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(
        max_length=100,blank=True,editable=False,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_code = models.CharField(
        max_length=20,blank=True,editable=False,unique=True)
    description = models.TextField(blank=True,null=True)
    mrp = models.FloatField()
    offer_price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='Product_Image')
    qr_image = models.ImageField(blank=True,upload_to='QR')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name

    def save(self, *args, **kwargs):
        if not self.id:
            product_code = randint(10000000, 99999999)
            self.product_code = product_code
            img = qrcode.make(f'http://www.bestroyal.com/product/{product_code}')
            b = img.save(f"media/QR/qr_{product_code}.png")
            # Newly created object, so set slug
            self.qr_image = f'QR/qr_{product_code}.png'
        super(Product, self).save(*args, **kwargs)
