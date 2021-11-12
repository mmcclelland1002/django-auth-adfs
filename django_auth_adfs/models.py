from django.db import models


class ActiveDirectoryConfig(models.Model):
    DIRECTORY_ROLES = "roles"
    SECURITY_GROUPS = "groups"

    GROUPS_CLAIM_CHOICES = (
        (DIRECTORY_ROLES, "Directory Roles"),
        (SECURITY_GROUPS, "Security Groups"),
    )

    USERNAME_CLAIM = "upn"

    USERNAME_CLAIM_CHOICES = (
        (USERNAME_CLAIM, "UPN"),
    )

    enabled = models.BooleanField("Enable/Disable Active Directory use", default=False)
    client_id = models.CharField(max_length=255)
    client_secret = models.CharField(max_length=255)
    tenant_id = models.CharField(max_length=255)
    mirror_groups = models.BooleanField(default=True)
    groups_claim = models.CharField(max_length=255, choices=GROUPS_CLAIM_CHOICES, default=GROUPS_CLAIM_CHOICES[0][0])
    username_claim = models.CharField(max_length=255, choices=USERNAME_CLAIM_CHOICES, default=USERNAME_CLAIM_CHOICES[0][0])

    def __str__(self) -> str:
        return self.tenant_id or ""

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)
        from django_auth_adfs.config import provider_config
        provider_config.load_config(force_reload=True)
        
    class Meta:
        verbose_name = "Active Directory config"
        verbose_name_plural = "Active Directory config"
