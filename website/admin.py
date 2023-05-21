from django.contrib import admin

from website.models import Category,FlashNews,Slider,Card,BreakingNews

# Register your models here.
admin.site.register(Category)
admin.site.register(FlashNews)
admin.site.register(Slider)
admin.site.register(Card)
admin.site.register(BreakingNews)