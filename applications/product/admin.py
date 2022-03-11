from django.contrib import admin
from django.utils.safestring import mark_safe

from applications.product.models import Product, ProductImage
from applications.review.models import Like


class InlineProductImage(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ['image', ]

# class InlineReviewImage(admin.TabularInline):
#     model = Like
#     extra = 1
#     fields = ['like', ]

class ProductAdminDisplay(admin.ModelAdmin):
    inlines = [InlineProductImage, ]
    list_display = ('title', 'in_stock', 'image', 'quantity')
    list_editable = ('in_stock', 'quantity')
    search_fields = ('title',)
    list_filter = ('category',)

    def image(self, obj):
        img = obj.image.first()
        if img:
            return mark_safe(f'<img src="{img.image.url}" width="80" height="80" style="object-fit: contain"/>')
        else:
            return ""


admin.site.register(Product, ProductAdminDisplay)


