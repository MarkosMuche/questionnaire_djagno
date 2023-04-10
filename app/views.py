from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from ai_utils.utils import get_vision_statement


class MainView(APIView):

    def post(self, request):

        data = request.data

        get_vision_statement(data)

        return Response(data)
        