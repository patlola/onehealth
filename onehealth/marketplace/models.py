from __future__ import unicode_literals

from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.


class BaseModel(models.Model):
    """Custom model to be inherited as base while making other models."""

    created = models.DateTimeField(
        auto_now_add=True, editable=False, db_index=True)
    modified = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True


def upload_build(self):
    return self.name + self.version_number


class Apps(BaseModel):
    """App model."""

    name = models.CharField(max_length=100, unique=True)
    version_number = models.DecimalField(validators=[MinValueValidator(0.0)], decimal_places=6, max_digits=9)
    build = models.FileField(upload_to=upload_build)
    webhook = models.URLField()

    def __unicode__(self):
        """Return name of entity."""
        return self.name

    class Meta:
        db_table = "apps"
        verbose_name = "App"
        verbose_name_plural = "Apps"
