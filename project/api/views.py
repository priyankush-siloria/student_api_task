from django.shortcuts import render
from rest_framework.views import APIView
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from .utils import randoem_name


class CreateListStudent(APIView):
    
    def get(self, request):
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        data = []
        for i in range(1000):
            first_name = randoem_name()
            last_name = randoem_name()
            request.data.update({"first_name": first_name, "last_name":last_name})
            serializer = StudentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
        

