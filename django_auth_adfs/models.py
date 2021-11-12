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

    enabled = models.BooleanField('Enable/Disable ActiveDirectory use', default=False)
    client_id = models.CharField(max_length=255, blank=True, null=True)
    client_secret = models.CharField(max_length=255, blank=True, null=True)
    tenant_id = models.CharField(max_length=255, blank=True, null=True)
    mirror_groups = models.BooleanField(default=True)
    groups_claim = models.CharField(max_length=255, choices=GROUPS_CLAIM_CHOICES, default=GROUPS_CLAIM_CHOICES[0][0])
    username_claim = models.CharField(max_length=255, choices=USERNAME_CLAIM_CHOICES, default=USERNAME_CLAIM_CHOICES[0][0])
    tenant_id = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self) -> str:
        return self.tenant_id

    class Meta:
        verbose_name = "Active Directory config"
        verbose_name_plural = "Active Directory config"
