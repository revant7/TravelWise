from django.shortcuts import render
from rest_framework import response, generics, status
from rest_framework.views import APIView
from . import serializers


# Create your views here.
class StudentListAPIView(generics.ListAPIView):
    serializer_class = serializers.StudentSerializer

    def get_queryset(self):
        return User.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
