from .models import Course, Instructor
from rest_framework import serializers

class CourseSerilizers(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Course
        fields= '__all__'



class InstructorSerilizers(serializers.HyperlinkedModelSerializer):
    # courses = CourseSerilizers(many=True, read_only = True)
    courses = serializers.HyperlinkedRelatedField(many=True, read_only = True, view_name='course-detail')

    class Meta:
        model = Instructor
        fields= '__all__'
        # fields= ['name', 'courses']