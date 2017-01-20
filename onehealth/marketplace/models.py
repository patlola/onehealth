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


def upload_build(self, filename):
    extension = filename[filename.rfind('.'):]

    return 'uploads/' + self.name + extension


def upload_logo(self, filename):

    extension = filename[filename.rfind('.'):]
    return 'images/' + self.name + extension


class Apps(BaseModel):
    """App model."""

    name = models.CharField(max_length=100, unique=True)
    version_number = models.DecimalField(validators=[MinValueValidator(0.0)], decimal_places=6, max_digits=9)
    build = models.FileField(upload_to=upload_build)
    webhook = models.URLField()
    logo = models.ImageField(upload_to=upload_logo)

    def __unicode__(self):
        """Return name of entity."""
        return self.name

    class Meta:
        db_table = "apps"
        verbose_name = "App"
        verbose_name_plural = "Apps"


class UserApp(BaseModel):
    """User App model."""

    practo_account = models.PositiveIntegerField(verbose_name='User')
    app = models.ForeignKey("Apps", related_name="users")

    def __unicode__(self):
        return self.app

    class Meta:
        db_table = "user_apps"
        verbose_name = "UserApp"
        verbose_name_plural = "UserApps"


class AppModels(BaseModel):
    app = models.ForeignKey("Apps")
    model_name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.model_name

    class Meta:
        db_table = "app_models"
        verbose_name = "AppModel"
        verbose_name_plural = "AppModels"


class AppModelFields(BaseModel):
    app_model = models.ForeignKey("AppModels")
    field_name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.field_name

    class Meta:
        db_table = "app_model_fields"
        verbose_name = "AppModelField"
        verbose_name_plural = "AppModelFields"


class UserData(BaseModel):
    """all the users data with apps."""

    practo_account = models.PositiveIntegerField()
    model_field = models.ForeignKey("AppModelFields")
    data_type = models.CharField(max_length=50)
    data = models.TextField()

    def __unicode__(self):
        return self.model_field

    class Meta:
        db_table = "user_data"
        verbose_name = "UserData"
        verbose_name_plural = "UserData"
