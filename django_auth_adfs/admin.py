from django.contrib import admin
from .models import ActiveDirectoryConfig


@admin.register(ActiveDirectoryConfig)
class ActiveDirectoryConfigAdmin(admin.ModelAdmin):
    list_display = ('tenant_id', 'client_id', 'enabled')
    list_filter = ('enabled',)
