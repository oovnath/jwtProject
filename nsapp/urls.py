
from django.contrib import admin
from django.urls import path
from .views import InstructorListView,CourseListView,CourseDetailView,InstructorDetailView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('Instructors', InstructorListView.as_view()),
    path('Course', CourseListView.as_view()),
    path('Course/<int:pk>', CourseDetailView.as_view(), name='course-detail'),
    path('Instructors/<int:pk>', InstructorDetailView.as_view(), name='instructor-detail'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
