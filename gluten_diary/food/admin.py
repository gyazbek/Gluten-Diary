from django.contrib import admin
from django.contrib import admin
from .models import Type, Brand, Food


class BrandInline(admin.TabularInline):
    model = Food.food_brands.through
    extra = 1

class TypeInline(admin.TabularInline):
    model = Food.food_types.through
    extra = 1

class FoodAdmin(admin.ModelAdmin):

    list_display = ('pk','title', 'created_on','reaction_scale','was_created_recently')
    list_filter = ['created_on']
    search_fields = ['title']


    fieldsets = [
        (None,               {'fields': ['author','title','notes','reaction_scale']}),
        ('Date information', {'fields': ['created_on']}),
    ]
    inlines = [BrandInline,TypeInline]
    readonly_fields = ['created_on']


admin.site.register(Food, FoodAdmin)
admin.site.register(Brand)
admin.site.register(Type)
