from django.contrib import admin
from .models import ActiveDirectoryConfig, GroupMapping


@admin.register(ActiveDirectoryConfig)
class ActiveDirectoryConfigAdmin(admin.ModelAdmin):
    list_display = ('tenant_id', 'client_id')

    def has_add_permission(self, *args, **kwargs):
        return not ActiveDirectoryConfig.objects.exists()


@admin.register(GroupMapping)
class GroupMappingAdmin(admin.ModelAdmin):
    filter_horizontal = ("groups",)
