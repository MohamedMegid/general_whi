from django.contrib import admin
from django.contrib.auth.models import Group , User
from core.models import Tutorial



admin.site.register(Tutorial)
admin.site.unregister(Group)
admin.site.unregister(User)
