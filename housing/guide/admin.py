from django.contrib import admin

from django.contrib.auth.models import User
from guide.models import *

admin.site.register(Dorm)
admin.site.register(Quote)
admin.site.register(Room)
