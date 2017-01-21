"""apps serializer."""
from marketplace.models import Apps
from rest_framework import serializers
from django.conf import settings


class AppsSerializer(serializers.ModelSerializer):
    """city serializers class for serializing the data for city."""

    install_url = serializers.SerializerMethodField()
    image_url = serializers.SerializerMethodField()
    build_path = serializers.SerializerMethodField()

    def get_install_url(self, obj):
        """a function to return the change in field name."""
        return settings.HOSTED_URL + obj.build.url

    def get_image_url(self, obj):
        return settings.HOSTED_URL + obj.logo.url

    def get_build_path(self, obj):
        return obj.build.path

    class Meta:
        model = Apps
        fields = ('id', 'name', 'install_url', 'image_url', 'build_path')
