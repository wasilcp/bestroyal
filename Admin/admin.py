from django.contrib import admin
from . import models
from django.urls import path,reverse
from django.conf.urls import url
from django.utils.html import format_html 
from django.shortcuts import get_object_or_404, HttpResponse
import qrcode

qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
# Register your models here.
class ProductAdmin(admin.ModelAdmin):   
     # add the link to the various fields attributes (fieldsets if necessary)
    readonly_fields = ('download_link','qr_image')
    list_display = ('product_name','qr_image','download_link')
    fields = ('product_name','description','mrp','offer_price','category','image')

    # add custom view to urls
    def get_urls(self):
        urls = super(ProductAdmin, self).get_urls()
        urls += [
            path('download-file/<int:pk>', self.download_file, 
                name='applabel_modelname_download-file'),
        ]
        return urls

    # custom "field" that returns a link to the custom function
    def download_link(self, obj):
        return format_html(
            '<a href="{}">Download file</a>',
            reverse('admin:applabel_modelname_download-file', args=[obj.id])
        )
    download_link.short_description = "Download file"

    # def regenerate_qr(self, obj):
    #     img = qrcode.make(f'http://www.wizzosaudi.com/product/{obj.product_code}')
    #     b = img.save(f"media/QR/qr_{obj.product_code}.png")
    #     # Newly created object, so set slug
    #     obj.qr_image = f'QR/qr_{obj.product_code}.png'
    #     obj.save()
    # regenerate_qr.short_description = "Regenerate QR image"

    # add custom view function that downloads the file
    def download_file(self, request, pk):
        obj = get_object_or_404(models.Product, id=pk)
        response = HttpResponse(obj.qr_image,content_type='application/force-download')
        response['Content-Disposition'] = f'attachment; filename={obj.qr_image}'
        # generate dynamic file content using object pk
        # response.write('whatever content')
        return response

admin.site.register(models.Category)
admin.site.register(models.Product, ProductAdmin)