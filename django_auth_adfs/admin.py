from django.contrib import admin
from .models import ActiveDirectoryConfig


@admin.register(ActiveDirectoryConfig)
class ActiveDirectoryConfigAdmin(admin.ModelAdmin):
    list_display = ('tenant_id', 'client_id')

    def has_add_permission(self, *args, **kwargs):
        return not ActiveDirectoryConfig.objects.exists()
