from django.conf import settings
from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from knox.models import AuthToken
from rest_framework.authtoken.models import Token
from .serializers import CandidateEnterSerializer,CandidateSerializer
# Create your views here.

class RegisterAPI(generics.GenericAPIView):
    serializer_class = CandidateEnterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": CandidateSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        # "token":Token.objects.get(user=user).key
        })
