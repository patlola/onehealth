"""apps serializer."""
from marketplace.models import Apps
from rest_framework import serializers


class AppsSerializer(serializers.ModelSerializer):
    """city serializers class for serializing the data for city."""

    install_url = serializers.SerializerMethodField()

    def get_install_url(self, obj):
        """a function to return the change in field name."""
        return 'http://onehealth.local' + obj.build.url

    class Meta:
        model = Apps
        fields = ('id', 'name', 'install_url')
