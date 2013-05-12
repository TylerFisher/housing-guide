from django.contrib import admin

from django.contrib.auth.models import User
from guide.models import *

class SlideShowImageInline(admin.StackedInline):
    model = SlideshowImage
    extra = 0

class DormAdmin(admin.ModelAdmin):
    inlines = [
        SlideShowImageInline,
    ]

admin.site.register(Dorm, DormAdmin)
admin.site.register(DormShapes)
admin.site.register(Quote)
