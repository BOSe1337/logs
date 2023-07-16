from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class UserAccessView(APIView):

    def post(self, request, *args, **kwargs):
        # return Response(request.META["REMOTE_ADDR"])
        return Response(request.META['HTTP_X_REAL_IP'])
    