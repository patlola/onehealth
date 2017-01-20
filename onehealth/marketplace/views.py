from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from marketplace.models import Apps
from marketplace.serializers.app_serializer import AppsSerializer


class AppList(APIView):

    def get(self, request):

        apps = Apps.objects.all()

        app_data = AppsSerializer(apps, many=True)

        return Response(app_data.data)
