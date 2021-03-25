#this is for serialization
from rest_framework import serializers
from courses.models import Course

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Course
        fields=('id','url','name','language','price')
