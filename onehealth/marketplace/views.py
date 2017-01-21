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
            action = request_data['action']
            try:
                app = Apps.objects.get(id=app_id)
            except Apps.DoesNotExist:
                app = None
            if app and app_id and action:
                if action == 'install':
                    user_app = UserApp.objects.get_or_create(practo_account=practo_account, app=app)
                else:
                    try:
                        user_app = UserApp.objects.get(practo_account=practo_account, app=app).delete()
                        return Response("Deleted")
                    except UserApp.DoesNotExist:
                        user_app = None
            else:
                user_app = None
        except KeyError:
            return Response("Data key Missing", status=status.HTTP_400_BAD_REQUEST)

        if (user_app and action == 'install') or action == 'uninstall':
            user_apps = UserApp.objects.filter(practo_account=practo_account)
            apps_data = []
            for user_app in user_apps:
                if user_app.app:
                    app_data = AppsSerializer(user_app.app)
                    apps_data.append(app_data.data)

            filenames = map(lambda x: x.get('build_path'), apps_data)
            app_ids = map(lambda x: str(x.get('id')), apps_data)
            app_id_string = "_".join(app_ids)

            with open('/tmp/' + app_id_string + '.txt', 'w') as outfile:
                for fname in filenames:
                    with open(fname) as infile:
                        for line in infile:
                            outfile.write(line)

            with open('/tmp/' + app_id_string + '.txt', 'r') as outfile:

                return Response(outfile.read())

        else:
            return Response("App DoesNotExist", 404)
