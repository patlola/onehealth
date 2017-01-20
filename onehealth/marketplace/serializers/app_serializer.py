"""apps serializer."""
from marketplace.models import Apps
from rest_framework import serializers
from django.conf import settings


class AppsSerializer(serializers.ModelSerializer):
    """city serializers class for serializing the data for city."""

    install_url = serializers.SerializerMethodField()
    logo_url = serializers.SerializerMethodField()

    def get_install_url(self, obj):
        """a function to return the change in field name."""
        return settings.HOSTED_URL + obj.build.url

    def get_logo_url(self, obj):
        return settings.HOSTED_URL + obj.logo.url

    class Meta:
        model = Apps
        fields = ('id', 'name', 'install_url', 'logo_url')
