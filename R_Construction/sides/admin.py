from django.contrib import admin

from .models import Side, SideIncharge, Work

admin.site.register(SideIncharge)
admin.site.register(Side)
admin.site.register(Work)
