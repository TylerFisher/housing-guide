from django.contrib import admin

from django.contrib.auth.models import User
from guide.models import *

class SlideShowImageInline(admin.StackedInline):
    model = SlideshowImage
    extra = 0

class QuoteInline(admin.StackedInline):
    model = Quote
    extra = 0

class DormAdmin(admin.ModelAdmin):
    inlines = [
        SlideShowImageInline,
        QuoteInline,
    ]

admin.site.register(Dorm, DormAdmin)
admin.site.register(Quote)
