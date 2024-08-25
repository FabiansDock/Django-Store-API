from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.contenttypes.admin import GenericTabularInline
from store.admin import ProductAdmin, ProductImageInline
from store.models import Product
from tags.models import TaggedItem
from .models import User


class TagInline(GenericTabularInline):
    model = TaggedItem
    extra = 1


class CustomProductAdmin(ProductAdmin):
    inlines = [ProductImageInline, TagInline]



@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2", "email", "first_name", "last_name"),
            },
        ),
    )

admin.site.unregister(Product)
admin.site.register(Product, CustomProductAdmin)
