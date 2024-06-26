from django.contrib import admin
from . models import Product, Variation, ReviewRating, productGallery
import admin_thumbnails
# Register your models here.

@admin_thumbnails.thumbnail('image')
class productGalleryInline(admin.TabularInline):
    model = productGallery
    extra = 1









class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}
    list_display = ('product_name', 'price', 'stock','category', 'modified_date', 'is_available')
    inlines = [productGalleryInline]

admin.site.register(Product, ProductAdmin)


class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'is_active')

    list_editable = ('is_active',)

    list_filter = ('product', 'variation_category', 'variation_value', 'is_active')





admin.site.register(Variation, VariationAdmin)

admin.site.register(ReviewRating)



admin.site.register(productGallery)