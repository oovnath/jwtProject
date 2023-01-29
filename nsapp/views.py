from django.shortcuts import render
from rest_framework import generics
from .serializers import CourseSerilizers, InstructorSerilizers
from .models import Instructor, Course
from rest_framework.permissions import IsAuthenticated,IsAdminUser,BasePermission



# Create your views here.

class writeByAdminOnlyPermision(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if request.method == 'GET':
            return True

        if request.method == 'POST' or request.method == 'PUT' or request.method == 'DELETE':
            if user.is_superuser:
                return True

        return False
        # return super().has_permission(request, view)
        

class InstructorListView(generics.ListCreateAPIView):
    serializer_class = InstructorSerilizers
    queryset = Instructor.objects.all()



class CourseListView(generics.ListCreateAPIView):
    # authentication_classes = [BasePermission]
    permission_classes=[IsAuthenticated,writeByAdminOnlyPermision]
    serializer_class = CourseSerilizers
    queryset = Course.objects.all()


class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class = CourseSerilizers
    queryset = Course.objects.all()

class InstructorDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InstructorSerilizers
    queryset = Instructor.objects.all()
