from django.contrib import admin
from shop.models import Product, Order

# Register your models here.
admin.site.site_header = "E-commerce Site"
admin.site.site_title = "ABC Shopping"
admin.site.index_title = "Manage ABC Shopping"


class ProductAdmin(admin.ModelAdmin):

    def change_catagory_to_default(self, request, queryset):
        queryset.update(catagory="default")

    change_catagory_to_default.short_description = "Default Category"
    list_display = (
        "title",
        "price",
        "discount_price",
        "catagory",
        "description",
    )
    search_fields = [
        "title",
        "catagory",
    ]
    actions = [
        "change_catagory_to_default",
    ]
    fields = ["title", "price"]
    list_editable = ["price", "catagory"]


admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
