from django.shortcuts import render
from rest_framework.views import APIView

class MainView(APIView):

    def post(self, request):

        data = request.data
        