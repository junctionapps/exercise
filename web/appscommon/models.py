from django.db import models
from django.contrib.auth.models import AbstractUser
from sitetree.models import TreeItemBase


class User(AbstractUser):
    """ Custom user based on Django best practices
    https://docs.djangoproject.com/en/1.10/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project
    """
    pass


class UserProfile(models.Model):
    """ Holds profile details for this user """
    pass


class CustomTreeItem(TreeItemBase):
    icon = models.CharField(max_length=256, blank=True,
                            help_text='FA or Glyph class for an icon. eg: "fa fa-th-large"')
