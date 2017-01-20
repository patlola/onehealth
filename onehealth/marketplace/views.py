from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from marketplace.models import Apps
from marketplace.models import AppModels, UserApp
from marketplace.serializers.app_serializer import AppsSerializer
# from marketplace.serializers.user_apps_serializer import
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

import json


class AppList(APIView):

    def get(self, request):

        apps = Apps.objects.all()

        app_data = AppsSerializer(apps, many=True)
        if app_data:
            return Response(app_data.data)
        else:
            return Response(404)


@method_decorator(csrf_exempt, name='dispatch')
class AppAction(APIView):

    def process_request(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)

    def get(self, request):
        query_paramters = request.query_params
        apps_data = []
        if query_paramters.get('practo_account'):
            user_apps = UserApp.objects.filter(practo_account=query_paramters.get('practo_account'))
            for user_app in user_apps:
                if user_app.app:
                    app_data = AppsSerializer(user_app.app)
                    apps_data.append(app_data.data)

        return Response(apps_data)

    def post(self, request):

        try:
            request_data = json.loads(request.body)
            practo_account = request_data['practo_account']
            app_id = request_data['app_id']
            try:
                app = Apps.objects.get(id=app_id)
            except Apps.DoesNotExist:
                app = None
            if app and app_id:
                user_app = UserApp.objects.get_or_create(practo_account=practo_account, app=app)
            else:
                user_app = None
        except KeyError:
            return Response("Data key Missing", status=status.HTTP_400_BAD_REQUEST)

        if user_app:
            return Response("created", 201)
        else:
            return Response("App DoesNotExist", 404)
